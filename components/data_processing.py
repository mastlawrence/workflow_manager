"""
Module to process underivatized semi-volatile extractable
data.
"""
import pandas as pd
import numpy as np
import sys

# Global settings
pd.options.mode.chained_assignment = None


def process_extractables(system_subset, AET_conc):
    """Process semi-volatile extractables data"""

    # Step 1: Select appropriate columns
    system_subset = select_columns(system_subset)

    # Step 2: ensure each column is of the correct format
    system_subset = format_dataframe(system_subset)

    # step 3: Assign labels to each injection
    assign_labels(system_subset)

    # Step 4: Calculate system suitability
    calculate_suitability(system_subset)

    # step 5: Perform semi-quantitation of the data
    system_subset = quantitate_data(system_subset, AET_conc)

    # step 6: Establish AET levels for the analysis
    AET_conc = establish_AET(system_subset)

    # step 7: Check to see if compound is above AET level
    check_for_AET(system_subset, AET_conc)

    # step 8: Divide system subset into separate conditions
    lowph_df = extract_condition(system_subset, "lowpH")
    highph_df = extract_condition(system_subset, "highpH")
    ipa_df = extract_condition(system_subset, "ipa")
    ipa50_df = extract_condition(system_subset, "ipa50")
    hexane_df = extract_condition(system_subset, "hexane")

    # step 9: subtract peaks observed in the blank injection
    lowph_df = subtract_condition(lowph_df)
    highph_df = subtract_condition(highph_df)
    ipa_df = subtract_condition(ipa_df)
    ipa50_df = subtract_condition(ipa50_df)
    hexane_df = subtract_condition(hexane_df)

    return [lowph_df, highph_df, ipa_df, ipa50_df, hexane_df]


def import_data(filename):
    """
    imports .csv file as a pandas data frame
    :param filename: a .csv MassHunter file
    :return: pandas data frame
    """
    return pd.read_csv(filename, skiprows=2)


def select_columns(dataframe):
    """
    Selects the columns of the MassHunter export data
    which are relevant for analysis
    :param dataframe: MassHunter file imported as data frame
    :return: dataframe subset
    """
    try:
        dataframe = dataframe[['File', 'RT', 'Name', 'Area', 'Formula', 'Score']]

    except TypeError:
        print("dataset did not successfully convert to Pandas dataframe. Exiting...")
        exit()

    return dataframe


def format_dataframe(dataframe):
    """
    Ensures that columns in the data frame are in the correct format
    :return: object of type dataframe
    """
    # Type-cast columns to strings
    dataframe['File'].astype(str)
    dataframe['Name'].astype(str)
    dataframe['Formula'].astype(str)

    # Type-cast columns to integers
    dataframe['RT'].astype(int)
    dataframe['Area'].astype(int)
    dataframe['Score'].astype(int)

    return dataframe


def assign_labels(dataframe):
    """
    Assign Empower-esque labels to each injection of the
    MassHunter dataframe
    :param dataframe:
    :return: object of type pandas dataframe
    """
    dataframe['labels'] = None

    # TODO: Figure out case-sensitivity
    _condition_selector(dataframe, 'blank', 'blank')
    _condition_selector(dataframe, 'sensitivity', 'sens')
    _condition_selector(dataframe, 'AET', 'AET')
    _condition_selector(dataframe, 'LowpH', 'lowpH')
    _condition_selector(dataframe, 'highpH', 'highpH')
    _condition_selector(dataframe, 'HighpH', 'highpH')
    _condition_selector(dataframe, 'IPA', 'ipa')
    _condition_selector(dataframe, '50IPA', 'ipa50')
    _condition_selector(dataframe, 'Hexane', 'hexane')

    return dataframe


def _condition_selector(dataframe, indicator, label):
    """
    Searches the 'file' column of the dataframe and updates the
    'labels' column based on the condition indicated by the 'file' column
    :param dataframe: a pandas dataframe
    :return: pandas dataframe
    """
    # TODO: See if you can abstract this a little bit more
    # TODO: Fix this to just query the value and not get the index value. R brain rot.

    # .str.contains() is looking for a particular subset or pattern
    # within the string being passed through, which is the contents of 'File'
    index = dataframe[dataframe['File'].str.contains(indicator)].index
    dataframe.loc[index, 'labels'] = label

    return dataframe


def calculate_suitability(dataframe):
    """
    Calculates blank interference and instrument precision to
    ensure values are within criteria.
    :param dataframe:
    :return: Type None
    """
    # TODO: Too much happening in this function, need to refactor
    # Calculate blank interference
    blank_data = dataframe[dataframe['labels'] == "blank"]
    AET_data = dataframe[dataframe['labels'] == 'AET']

    test_blank_value = int(blank_data['Area'].iloc[0])
    test_AET_value = list(AET_data['Area'])

    blank_value = round(test_blank_value, 2)

    AET_value = sum(test_AET_value) / len(test_AET_value)
    AET_value = round(AET_value, 2)

    blank_interference = round((blank_value / AET_value) * 100, 2)
    print("Blank interference is calculated to be:", blank_interference, "%")

    if blank_interference < 10:
        print("Blank interference passes")

    else:
        print("System suitability fails for blank interference")

    rsd_calculation = round(np.std(test_AET_value) / (sum(test_AET_value) / len(test_AET_value)), 2)
    print("RSD calculation:", rsd_calculation, "%")

    if rsd_calculation < 15.0:
        print("RSD calculation passes")

    else:
        print("System suitability fails for percent RSD")

    return None


def quantitate_data(df, AET_conc):
    """
    Uses concentration of Irganox 1010 standard to perform
    semi-quantitation of extractables data
    :param df: Pandas Dataframe
    :return: Object of type Pandas Dataframe
    """
    # Takes user input
    try:
        std_conc = AET_conc

    except ValueError:
        print("Invalid concentration, value must be numeric!")
        sys.exit()

    # calculates standard area
    std_area = df[df['labels'] == 'AET']
    std_area = list(std_area['Area'])
    avg_area = round(sum(std_area) / len(std_area), 2)

    # perform semi-quantitation
    df['concentration'] = round((df['Area'] / avg_area) * std_conc, 4)

    return df


def establish_AET(df):
    """
    Parses the system subset dataframe and establishes a representative
    AET value based on system subset data.
    :param df:
    :return:
    """
    AET_df = df[df['labels'] == "AET"]
    AET_conc = round(sum(AET_df['concentration']) / len(AET_df['concentration']), 4)
    print("Average AET concentration is:", AET_conc)

    return AET_conc


def check_for_AET(df, AET):
    """
    Check each compound to determine whether it is above AET concentration or
    not.
    :param df: system subset dataframe
    :param AET: calculated AET level
    :return: object of type Pandas Dataframe
    """
    df['above_aet'] = None

    # TODO: Figure out conditional statement for this
    index = df[df['concentration'] > AET].index
    df.loc[index, 'above_aet'] = "yes"

    index = df[df['concentration'] < AET].index
    df.loc[index, 'above_aet'] = "no"

    return df


def extract_condition(df, label):
    """
    Divide the system subset into separate conditions
    :param df: Pandas dataframe
    :return: object of type Pandas dataframe
    """
    condition_index = df[df['labels'] == label]

    return condition_index


def subtract_condition(df_subset):
    """
    Separates condition into blank and sample dataframes,
    matching on
    :param df_subset: dataset subset to one condition
    :return: blank-subtracted data frame
    """
    # Create blank index
    blank_index = df_subset['File'].str.contains('blank')

    # separate the condition
    df_blank = df_subset[blank_index]
    df_sample = df_subset[-blank_index]

    # join two data frames and subtract
    # TODO: I'm sure replacing NaNs with 0 will not cause problems down the road
    df_sub = pd.merge(df_sample, df_blank, on='Name', how='outer')
    df_sub.fillna(0, inplace=True)

    df_sub['corrected_area'] = df_sub['Area_x'] - df_sub['Area_y']
    df_sub['corrected_conc'] = df_sub['concentration_x'] - df_sub['concentration_y']

    # get rid of unused columns
    df_sub = df_sub[['File_x', 'RT_x', 'Name', 'Formula_x', 'Score_x', 'labels_x',
                     'corrected_area', 'corrected_conc']]

    # rename columns
    df_sub = df_sub.rename(columns={'File_x': 'File', 'RT_x': 'RT', 'Formula_x': 'Formula',
                                    'Score_x': 'Score', 'labels_x': 'Labels'})

    return df_sub

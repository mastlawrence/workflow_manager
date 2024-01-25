"""
module to process volatile extractable data from headspace analysis
"""
import data_processing


def main(dataset, AET_conc):
    """Process volatile extractables data"""
    # TODO: Blank subtraction is going to have to be handled differently with no control

    # Step 0: Import data as Pandas dataframe
    system_subset = data_processing.import_data(dataset)

    # Step 1: Select the appropriate columns
    system_subset = data_processing.select_columns(system_subset)

    # Step 2: Assign labels to injections
    assign_labels_vol(system_subset)

    # Step 3: Calculate system suitability
    data_processing.calculate_suitability(system_subset)

    # TODO: Maybe try putting blank subtraction right here?
    # Step 3.5: correct for method blank
    subtract_blank_volatile(system_subset)



    # step 4: Perform semi-quantitation
    data_processing.quantitate_data(system_subset, AET_conc)

    # step 5: Establish AET levels for the analysis
    AET_conc = data_processing.establish_AET(system_subset)

    # step 6: Check to see if compounds are above AET concentration
    data_processing.check_for_AET(system_subset, AET_conc)


def assign_labels_vol(dataframe):
    """
    assigns labels to the volatile extractable samples
    :return: Pandas dataframe
    """
    data_processing._condition_selector(dataframe, 'blank', 'blank')
    data_processing._condition_selector(dataframe, 'sensitivity', 'sens')
    data_processing._condition_selector(dataframe, 'AET', 'AET')

    # TODO: Find a smarter way to do this
    data_processing._condition_selector(dataframe, 'S24', 'sample')
    data_processing._condition_selector(dataframe, 'S23', 'sample')

    return dataframe


def subtract_blank_volatile(dataframe):
    """
    Corrects the volatile dataset using the blank injections
    :param dataframe: A pandas dataframe of volatiles data
    :return: object of type Pandas dataframe
    """
    print("test of the function")

    pass

if __name__ == "__main__":
    main('test_vol.csv', 3.0)

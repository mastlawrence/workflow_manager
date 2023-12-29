"""
Utility of the extractables page
"""
# TODO: Figure out how to get the card options to separate out
import reflex as rx


def extractables_menu():
    """
    Controls the menu on the extractables page.
    """

    volatile_text = """
        submit processed volatile extractables data in .csv format with the reporting requirements
        present within the table 
        """

    semivolatile_text = """
        submit processed semivolatile extractables data in .csv format with the reporting requirements
        present within the table 
        """

    nonvolatile_text = """
        submit processed nonvolatile extractables data in .csv format with the reporting requirements
        present within the table 
        """

    return rx.vstack(
        rx.card(
            rx.text(volatile_text),
            header=rx.heading(rx.link("Submit Volatile Data", href='/submission_lch'), size='lg',
                              style={'font-family': 'Tahoma', 'font-weight': '500'}),

            size='lg',
            style={'font-family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'lightgreen',
                    'transition': '0.3s'}
        ),

        rx.card(
            rx.text(semivolatile_text),
            header=rx.heading(rx.link("Submit Semi-Volatile Data", href='/submission_lch'), size='lg',
                              style={'font-family': 'Tahoma', 'font-weight': '500'}),

            size='lg',
            style={'font-family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'lightblue',
                    'transition': '0.3s'}
        ),

        rx.card(
            rx.text(nonvolatile_text),
            header=rx.heading(rx.link("Submit Non-Volatile Data", href='/submission_lch'), size='lg',
                              style={'font-family': 'Tahoma', 'font-weight': '500'}),

            size='lg',
            style={'font-family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'LightGrey',
                    'transition': '0.3s'}
        ),
        justify_content='space-between'
    )

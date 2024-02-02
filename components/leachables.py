"""
Utility of the leachables page
"""
import reflex as rx


def leachables_menu():
    """
    defines the leachables webpage
    :return: object type NULL
    """

    lch_card_1 = """
    Submit processed volatile leachables data in .csv format with the reporting requirements
    present within the table.
    """

    lch_card_2 = """
    Submit processed semi-volatile leachables data in .csv format with the reporting requirements
    present within the table.
    """

    lch_card_3 = """
    Submit processed non-volatile leachables data in .csv format with the reporting requirements
    present within the table.
    """

    return rx.vstack(
        rx.card(
            rx.text(lch_card_1),
            header=rx.heading("Submit Volatile Leachables Data", size='lg',
                              style={'font-family': 'monospace', 'font-weight': '500'}),
            size='lg',
            style={'font-family': 'monospace'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'PaleGreen',
                    'transition': '0.3s'}
        ),

        rx.card(
            rx.text(lch_card_2),
            header=rx.heading("Submit Semi-Volatile Leachables Data", size='lg',
                              style={'font-family': 'monospace', 'font-weight': '500'}),
            size='lg',
            style={'font-family': 'monospace'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'LightBlue',
                    'transition': '0.3s'}
        ),

        rx.card(
            rx.text(lch_card_3),
            header=rx.heading("Submit Non-Volatile Leachables Data", size='lg',
                              style={'font-family': 'monospace', 'font-weight': '500'}),
            size='lg',
            style={'font-family': 'monospace'},
            width='800px',
            border='2px solid',
            _hover={'background-color': 'LightGrey',
                    'transition': '0.3s'}
        ),
        justify_content='space-between'
    )

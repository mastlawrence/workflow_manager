"""
Utility of the leachables page
"""
import reflex as rx


def leachables_menu():
    """
    defines the leachables webpage
    :return: object type NULL
    """
    return rx.vstack(
        rx.card(
            rx.text("card 1"),
            header=rx.heading("Process Leachables Data", style={'font-family': 'Tahoma', 'font-weight': '500'}),
            size='lg',
            style={'font-family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'PaleGreen',
                    'transition': '0.3s'}
        ),

        rx.card(
            rx.text("card 2"),
            header=rx.heading("This is card 2", style={'font-family': 'Tahoma', 'font-weight': '500'}),
            size='lg',
            style={'font-family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'LightBlue',
                    'transition': '0.3s'}
        ),

        rx.card(
            rx.text("card 3"),
            header=rx.heading("this is card 3", style={'font-family': 'Tahoma', 'font-weight': '500'}),
            size='lg',
            style={'font-family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background-color': 'LightGrey',
                    'transition': '0.3s'}
        ),
        justify_content='space-between'
    )

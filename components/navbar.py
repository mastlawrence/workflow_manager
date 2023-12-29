"""
navbar function for the application
"""
import reflex as rx


def navbar():
    return rx.flex(
        rx.box(
            rx.image(src='/thesis_logo.PNG')
        )
    )


def main_menu():
    """
    main menu design
    :return: navigation menu object
    """

    extractables_txt = """
    Manage MassHunter data of extractables compounds from primary packaging
    systems. Review and update extractables RRT databases for non-volatile,
    semi-volatile, and non-volatile compounds. Review literature regarding
    analysis of extractables compounds in primary packaging systems.
    """

    leachables_txt = """
    Manage MassHunter data of leachables compounds from device and drug 
    product studies. Review previous leachables profiles and validation
    studies. Review ICH and FDA expectations of leachables validation
    acceptance criteria.
    """

    literature_txt = """
    Review extractables and leachables literature from outside studies. 
    Search for references to compounds identified in extractables studies.
    Read about previous work performed on similar primary packaging systems.
    """

    return rx.vstack(
        rx.card(
            rx.text(extractables_txt),
            header=rx.heading(rx.link("Extractables", href='/extractables'),
                              rx.image(src='bottle1.PNG', width='60px', display='inline-block', style={'margin-left': '30px'}),
                              size='lg', style={'font_family': 'Tahoma', 'font_weight': '500'}),
            style={"font_family": "Tahoma"},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'PaleGreen',
                    'transition': '0.3s'},
        ),
        rx.card(
            rx.text(leachables_txt),
            header=rx.heading(rx.link("Leachables", href='/leachables'),
                              rx.image(src='/chem_illustration.PNG', width='70px', display='inline-block', style={'margin-left': '40px'}),
                              size='lg', style={'font_family': 'Tahoma', 'font_weight': '500'}),
            style={'font_family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'LightBlue',
                    'transition': '0.3s'}
        ),
        rx.card(
            rx.text(literature_txt),
            header=rx.heading(rx.link("Literature", href='/literature'),
                              rx.image(src='/book_icon.PNG', width='70px', display='inline-block', style={'margin-left': '55px'}),
                              size='lg', style={'font_family': 'Tahoma', 'font_weight': '500'}),
            style={'font_family': 'Tahoma'},
            width='800px',
            border='2px solid',
            _hover={'background_color': 'LightGrey',
                    'transition': '0.3s'}
        ),
        justify_content='space_between'
    )

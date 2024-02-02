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

    stability_text = """
    Review extractables and leachables literature from outside studies. 
    Merge extractables and leachables studies across multiple timepoints 
    into a single report. Search for references to compounds identified 
    in extractables studies. Read about previous work performed on similar
     primary packaging systems.
    """

    return rx.vstack(
        rx.card(
            rx.text(extractables_txt, font_size="15"),
            header=rx.heading(rx.link("Extractables", href='/extractables'),
                              rx.image(src='bottle1_transparent.PNG', width='80px', display='inline-block', style={'margin-left': '30px'}),
                              size='lg', style={'font_family': 'monospace', 'font_weight': '800'}),
            style={"font_family": "monospace"},
            width='900px',
            border='2px solid',
            _hover={'background_color': 'PaleGreen',
                    'transition': '0.3s'},
        ),
        rx.card(
            rx.text(leachables_txt, font_size="15"),
            header=rx.heading(rx.link("Leachables", href='/leachables'),
                              rx.image(src='/chem_illustration_transparent.PNG', width='90px', display='inline-block', style={'margin-left': '40px'}),
                              size='lg', style={'font_family': 'monospace', 'font_weight': '800'}),
            style={'font_family': 'monospace'},
            width='900px',
            border='2px solid',
            _hover={'background_color': 'LightBlue',
                    'transition': '0.3s'}
        ),
        rx.card(
            rx.text(stability_text, font_size="15"),
            header=rx.heading(rx.link("Stability", href='/literature'),
                              rx.image(src='/book_icon_transparent.PNG', width='90px', display='inline-block', style={'margin-left': '55px'}),
                              size='lg', style={'font_family': 'monospace', 'font_weight': '800'}),
            style={'font_family': 'monospace'},
            width='900px',
            border='2px solid',
            _hover={'background_color': 'LightGrey',
                    'transition': '0.3s'}
        ),
        # justify_content='space_between'
    )

"""
Extractables and Leachables Workflow Manager v.0.00.01
Author: Matthew St. Lawrence
Date: 13Nov2023
Application to manage extractables workflow
"""
import os
import reflex as rx
import pandas as pd
from typing import List
from components.navbar import navbar, main_menu
from components.extractables import extractables_menu
from components.leachables import leachables_menu
from components.data_processing import process_extractables


class State(rx.State):
    """The application state"""
    # TODO: GO through this class and understand it

    uploaded_file_path: str = ""
    number: float

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the upload of an excel file"""
        # TODO: Go through this and understand this upload system more

        file = files[0]
        data = await file.read()
        outfile = rx.get_asset_path(file.filename)

        with open(outfile, 'wb') as f:
            f.write(data)

        self.uploaded_file_path = outfile



    def process_volatile(self, filename, AET_conc):
        """processes volatile data"""

        pass

    def process_semivol(self, filename, AET_conc):
        """Process semi-volatile data"""

        finished_data = pd.read_csv(filename, skiprows=2)
        finished_data = process_extractables(finished_data, AET_conc)

        # TODO: Figure out the smart way to do this
        finished_data[0].to_csv(".web/public/finished_lowpH.csv", index=False)
        finished_data[1].to_csv(".web/public/finished_highpH.csv", index=False)
        finished_data[2].to_csv(".web/public/finished_IPA.csv", index=False)
        finished_data[3].to_csv(".web/public/finished_50IPA.csv", index=False)
        finished_data[4].to_csv(".web/public/finished_hexane.csv", index=False)


def index():
    """
    creates home page of application
    """
    return rx.container(
        navbar(),
        main_menu()
    )


def ext_page():
    """
    test of the extractables page
    """
    return rx.container(
        rx.image(src='/thesis_logo.PNG'),
        extractables_menu(),
    )


def lch_page():
    """
    test of the leachables page
    """
    return rx.container(
        rx.image(src='/thesis_logo.PNG'),
        leachables_menu()
    )


def lit_page():
    """
    test of the literature review page
    """
    return rx.container(
        rx.image(src='/thesis_logo.PNG'),
        rx.text("You made it to the literature review page!")
    )


def ext_submission():
    """
    Page where analyst is to submit processed extractables data
    """
    return rx.container(
        rx.image(src='/thesis_logo.PNG'),
        rx.box(
            rx.upload(
                rx.text("drag and drop file here or click to select files"),
                border='1px dotted',
                padding='5em'
            ),
        ),
    )


def volatiles():
    """
    Landing page for submitting volatiles data
    """
    return rx.vstack(
        navbar(),

    )


def semivolatile():
    """
    page where analyst is to submit processed leachables data
    """
    # TODO: Add markers to passing or failing system suitability on-screen
    # TODO: Organize this code better by importing from another module
    return rx.vstack(
        navbar(),
        # rx.clear_selected_files,
        rx.form(
            rx.vstack(
                rx.upload(
                    rx.card(
                        rx.text("drag and drop file here or click to select files"),
                        border='1px dotted',
                        padding='5em',
                    )),
                rx.hstack(
                    rx.text("Actual AET Concentration (µg/mL):"),
                    rx.number_input(on_change=State.set_number),
                ),
                rx.hstack(
                    rx.text("Notebook Reference:", width='300px'),
                    rx.input()
                ),
                rx.button_group(
                    rx.button("Submit", on_click=lambda: State.handle_upload(rx.upload_files())),

                    # TODO: SO damn close here, just need to get the .csv filename to be abstracted
                    rx.button("Process Data",
                              on_click=lambda: State.process_semivol(rx.get_asset_path("test_data.csv"), State.number)),
                    variant='outline',
                ),
                rx.button_group(
                    rx.button("Download Low pH", on_click=rx.download(url='/finished_lowpH.csv')),
                    rx.button("Download High pH", on_click=rx.download(url='/finished_highpH.csv')),
                    rx.button("Download 50% IPA", on_click=rx.download(url='/finished_50IPA.csv')),
                    rx.button("Download 100% IPA", on_click=rx.download(url='/finished_IPA.csv')),
                    rx.button("Download 100% Hexane", on_click=rx.download(url='/finished_hexane.csv')),
                    variant='outline'
                ),
                # rx.text(rx.get_asset_path("test_data.csv")),
            )
        )
    )

print(State.uploaded_file_path)

def test_page():
    """
    page for testing the upload of files
    """
    return rx.fragment(
        rx.text("This is a test page"),
        rx.upload("upload excel file"),
        rx.button("submit data", on_click=lambda: State.handle_upload(rx.upload_files())),
        rx.text(f"uploaded file path: {State.uploaded_file_path}")
    )


app = rx.App()

app.add_page(index, route='/')
app.add_page(test_page, route='/test')
app.add_page(ext_page, route='/extractables')
app.add_page(lch_page, route='/leachables')
app.add_page(lit_page, route='/literature')
app.add_page(ext_submission, route='/submission_ext')
app.add_page(volatiles, route='/volatiles')
app.add_page(semivolatile, route='/submission_semi')

app.compile()

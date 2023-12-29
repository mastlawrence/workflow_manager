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

    img: list[str]

    # why this decorator?
    @rx.var
    def file_str(self) -> str:
        """Get the string representation of the uploaded files"""
        return "\n".join(os.listdir(rx.get_asset_path()))

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the upload of a file"""

        for file in files:
            upload_data = await file.read()

            outfile = rx.get_asset_path(file.filename)
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)


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
        extractables_menu()
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


def lch_submission():
    """
    page where analyst is to submit processed leachables data
    """
    return rx.vstack(
        rx.image(src='/thesis_logo.PNG'),
        rx.clear_selected_files,
        rx.form(
            rx.vstack(
                rx.upload(
                    rx.card(
                        rx.text("drag and drop file here or click to select files"),
                        border='1px dotted',
                        padding='5em',
                    )),
                # TODO: Figure out what this line of code does
                rx.button("Submit", on_click=lambda: State.handle_upload(rx.upload_files())),
                rx.button("process data"),
                rx.text(State.file_str)
            )
        )
    )


def retrieve_data(file_in_name):
    """
    Pulls in .csv data after being submitted through the web app
    :return: Object of Type None
    """
    # TODO: Big stuff happening here, but needs to be cleaned up.
    # TODO: Abstract the name out so the program is only looking for .csv files
    file_dir = os.listdir(rx.get_asset_path())

    try:
        # Step 1: finds the loaded .csv files
        print("file successfully mounted")
        search_index = file_dir.index(file_in_name)
        file_location = file_dir[search_index]

        # displays the asset path for debugging
        outfile = rx.get_asset_path(file_location)
        print(outfile)

        # Step 2: read submitted file located by step 1
        system_df = pd.read_csv(outfile, skiprows=2)

        # Step 3: Process the data file
        system_df = process_extractables(system_df)

        print(system_df)

        # Step 4: write file to app memory
        # TODO: Update the formatting of this to allow for the naming of the written file
        filepath = '.web/public/processed_data.csv'
        system_df.to_csv(filepath, index=False)

        # Print the state of the app's memory for debugging purposes
        print(os.listdir(rx.get_asset_path()))

        return None

    except ValueError:
        print("no .csv file mounted")
        pass


app = rx.App()

app.add_page(index, route='/')
app.add_page(ext_page, route='/extractables')
app.add_page(lch_page, route='/leachables')
app.add_page(lit_page, route='/literature')
app.add_page(ext_submission, route='/submission_ext')
app.add_page(lch_submission, route='/submission_lch')

# TODO: Write the back-end of this
system_subset = retrieve_data('test_data.csv')

app.compile()

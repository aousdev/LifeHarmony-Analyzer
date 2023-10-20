import re
import gspread
from prettytable import PrettyTable
from core.google_sheets import SHEET
from core.helpers import normalize_data


def get_data_for_entred_inputs(entered_date, entered_gender, entered_age_range):
    """
    Retrieve and calculate a score based on data for a given date, gender and age_range.

    Args:
        entered_date (str): The entered date.
        entered_gender (str): The entered user gender ('Female' or 'Male').
        entered_age_range (str): The entered age range

    Returns:
        None
    """
    try:
        # Open the 'main' worksheet
        main_worksheet = SHEET.worksheet("main")

        # Get all the values from the worksheet
        data = main_worksheet.get_all_values()

        normalize_data(data)

        # Check if the 'Timestamp' column exists
        if "Timestamp" not in data[0]:
            print("Timestamp column not found in the sheet.")
            return

        # Find the indices of the 'Timestamp' and 'Gender'
        timestamp_column_index = data[0].index("Timestamp")
        gender_column_index = data[0].index("GENDER")
        age_column_index = data[0].index("AGE")

        # Filter the data based on timestamp, gender and age_range
        filtered_data, headings = filter_data_by_criteria(
            data,
            entered_date,
            entered_gender,
            entered_age_range,
            timestamp_column_index,
            gender_column_index,
            age_column_index,
        )

        # Create the first PrettyTable object with the timestamp, gender, and age
        table1 = PrettyTable()
        table1.field_names = ["Timestamp", "Gender", "Age"]
        table1.add_row([entered_date, entered_gender, entered_age_range])
        print(table1)
        filtered_headings = [
            headings[i]
            for i in range(len(headings))
            if i not in [timestamp_column_index, gender_column_index, age_column_index]
            and headings[i] != ""
        ]

        # Exclude specific columns (Age, Gender, and Timestamp) from filtered_data
        excluded_columns = [
            age_column_index,
            gender_column_index,
            timestamp_column_index,
        ]
        filtered_data_without_excluded_columns = [
            [
                cell
                for i, cell in enumerate(row)
                if i not in excluded_columns and cell != ""
            ]
            for row in filtered_data
        ]
        if filtered_data_without_excluded_columns:
            for row in filtered_data_without_excluded_columns:
                # Create PrettyTable objects for all sets of data
                table = PrettyTable(filtered_headings)
                table.add_row(row)
                print(table)

            score = 42.0
            # Display the calculated score
            print(f"Calculated Score: {score}")
        else:
            print("No data found based on the provided criteria.")
    except gspread.exceptions.WorksheetNotFound:
        print("Worksheet 'main' not found in the Google Sheet.")


def filter_data_by_criteria(
    data,
    date,
    gender,
    age_range,
    timestamp_column_index,
    gender_column_index,
    age_column_index,
):
    """
    Filter the data based on date, gender, and age range.

    Args:
        data (list): The data to be filtered.
        date (str): The entered date.
        gender (str): The entered user gender ('Female' or 'Male').
        age_range (str): The entered age range
        timestamp_column_index (int): Index of the 'Timestamp' column in the data.
        gender_column_index (int): Index of the 'Gender' column in the data.
        age_column_index (int): Index of the 'Gender' column in the data.

    Returns:
        tuple: A tuple containing the filtered data (list) and the headings (list).
    """
    min_age, max_age = map(int, age_range.split(","))
    filtered_data = []
    headings = data[0]
    for row in data[1:]:
        row_timestamp = row[timestamp_column_index]
        row_gender = row[gender_column_index]
        row_age = row[age_column_index]
        if (
            row_timestamp == date
            and row_gender.strip() == gender
            and (
                (
                    re.match(r"^(\d+)\+$", row_age)
                    and min_age <= int(row_age.split("+")[0])
                )
                or min_age <= int(row_age.split("-")[0]) <= max_age
                # Check if age is in the "min+" format and is greater than or equal to min_age
            )
        ):
            filtered_data.append(row)
    return filtered_data, headings


def calculate_score(data):
    """
    Calculate the WORK_LIFE_BALANCE_SCORE for the given data

    Args:
        data (list): The filtered data for the entered date.

    Returns:
        float: The calculated score.
    """
    # TO-DO: WORK_LIFE_BALANCE_SCORE calculation logic
    score = 42.0

    return score

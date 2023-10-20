from datetime import datetime
import re


def is_valid_date(date_str):
    """
    Check if the entered date string is valid and in the format 'DD/MM/YY'.

    Args:
        date_str (str): The date string to be validated.

    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    try:
        # Attempt to parse the date in the 'DD/MM/YY' format
        datetime.strptime(date_str, "%d/%m/%y")
        return True
    except ValueError:
        return False


def normalize_data(data):
    """
    Normalize the age data in the provided dataset.

    This function iterates through the rows of the dataset and normalizes the age values
    in the specified column (index 21) according to predefined patterns. The normalized
    age values are then updated in the dataset.

    Args:
        data (list of lists): The dataset containing rows of data.

    Returns:
        None
    """
    # Assuming Age column is in the 22nd column (index 21)
    for row in data:
        age_data = row[21]  # Assuming Age is in the 22nd column (index 21)
        normalized_age = normalize_age(age_data)
        row[21] = normalized_age  # Update the Age column with the normalized value


def normalize_age(age_str):
    """
    Normalize an age string using predefined patterns.

    This function takes an age string as input and normalizes it according to predefined patterns.
    The patterns include "min to max," "Less than max," and "min or more." The function uses regular
    expressions to identify the pattern and applies the appropriate normalization.

    Args:
        age_str (str): The age string to be normalized.

    Returns:
        str: The normalized age string.
    """
    # Regular expressions to match the patterns
    min_max_pattern = r"(\d+)\s*to\s*(\d+)"
    less_than_max_pattern = r"Less\s*than\s*(\d+)"
    min_or_more_pattern = r"(\d+)\s*or\s*more"

    # Check for each pattern and normalize accordingly
    if re.match(min_max_pattern, age_str):
        match = re.match(min_max_pattern, age_str)
        min_age = match.group(1)
        max_age = match.group(2)
        return f"{min_age}-{max_age}"
    elif re.match(less_than_max_pattern, age_str):
        match = re.match(less_than_max_pattern, age_str)
        max_age = match.group(1)
        return f"18-{max_age}"
    elif re.match(min_or_more_pattern, age_str):
        match = re.match(min_or_more_pattern, age_str)
        min_age = match.group(1)
        return f"{min_age}+"
    else:
        # If none of the patterns match, return the original string
        return age_str

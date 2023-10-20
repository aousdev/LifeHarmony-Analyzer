import re
from colorama import Fore
import signal
from core.helpers import is_valid_date
from core.data_processing import get_data_for_entred_inputs

exit_requested = False  # Initialize the exit flag


def get_user_inputs():
    """
    Prompt the user for date and gender inputs.

    Returns:
        None
    """
    global exit_requested
    try:
        while not exit_requested:
            while True:
                entered_date = input(
                    "Enter a date (in the format 'DD/MM/YY') or 'exit' to quit: "
                ).strip()

                if entered_date.lower() == "exit":
                    print("Exiting the program.")
                    exit_requested = True
                    break  # Exit the inner loop

                if is_valid_date(entered_date):
                    break
                else:
                    print(
                        Fore.RED
                        + "Invalid date format. Please enter a valid date in the format 'DD/MM/YY'."
                    )

            if exit_requested:
                print("exit requested")
                break

            while True:
                entered_gender = (
                    input("Enter the gender you want to filter with (Female/Male): ")
                    .strip()
                    .title()
                )
                if entered_gender in ["Female", "Male"]:
                    break
                else:
                    print(
                        Fore.RED
                        + "Invalid gender input. Please enter 'Female' or 'Male'."
                    )

            while True:
                entered_age_range_input = input(
                    "Enter the age range you want to filter with in the following format: min,max: "
                ).strip()
                # Check if the input matches the "min,max" format using a regular expression
                if re.match(r"^\d+,\d+$", entered_age_range_input):
                    break  # Break the loop if the format is valid
                else:
                    print(
                        Fore.RED
                        + "Invalid format. Please enter the age range in the format 'min,max'."
                    )

            if not exit_requested:
                get_data_for_entred_inputs(entered_date, entered_gender, entered_age_range_input)
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting the program.")
        return  # Exit the function on Ctrl+C


# Set up a signal handler for Ctrl+C
signal.signal(signal.SIGINT, lambda signal, frame: exit())

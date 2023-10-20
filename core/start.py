from core.user_interface import get_user_inputs

def banner():
    """
    Display a custom ASCII art banner.

    This function displays a custom ASCII art banner with decorative text and graphics.
    The banner is designed to add a visual element to the program's interface and enhance its appearance.

    Args:
        None

    Returns:
        None
    """
    font = """

 _     _  __     _   _                                           ___              _                    
| |   (_)/ _|   | | | |                                         / _ \            | |                   
| |    _| |_ ___| |_| | __ _ _ __ _ __ ___   ___  _ __  _   _  / /_\ \_ __   __ _| |_   _ _______ _ __ 
| |   | |  _/ _ \  _  |/ _` | '__| '_ ` _ \ / _ \| '_ \| | | | |  _  | '_ \ / _` | | | | |_  / _ \ '__|
| |___| | ||  __/ | | | (_| | |  | | | | | | (_) | | | | |_| | | | | | | | | (_| | | |_| |/ /  __/ |   
\_____/_|_| \___\_| |_/\__,_|_|  |_| |_| |_|\___/|_| |_|\__, | \_| |_/_| |_|\__,_|_|\__, /___\___|_|   
                                                         __/ |                       __/ |             
                                                        |___/                       |___/              
 """
    print(font)

def start():
    """
    Main program logic for interacting with the LifeHarmony Analyzer.
    Allows the user to enter a date, view data for that date, and filter by gender and age range.
    """
    banner()
    get_user_inputs()

start()

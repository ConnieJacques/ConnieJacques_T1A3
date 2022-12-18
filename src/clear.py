import os

# Clear terminal window
def clear():
    # Check if the operating system is Linux/Mac or Windows
    # If Linux or Mac use the command clear to clear the terminal
    if os.name == 'posix':
            os.system('clear')
    else:
        # Otherwise, use the command cls to clear the terminal window
        os.system('cls')
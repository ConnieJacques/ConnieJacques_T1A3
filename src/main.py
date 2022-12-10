import os
from time import sleep
# from main_menu import *

clear_terminal()

print("Welcome to the Guessing Game.\nYou will be asked a series of trivia questions that relate to different decades and years from the last 100 years. Answer the questions correctly with relation to your year of birth to see if we can guess your age correctly.\nPress ENTER to continue.")

if input() == "":
    clear_terminal()
    # if os.name == 'posix':
    #     os.system('clear')
    # elif not os.name == 'posix':
    #     os.system('cls')
else:
    sleep(5)

# Get and validate user's name
def get_user_name():
    print("To begin, please enter your name:")
    while True:
        user_name = input()
        if not user_name.isalpha():
            print("Please enter your name:")
            continue
        else:
            return user_name

get_user_name()

clear_terminal()

def main_menu():
    try:
        print(f"Hi {get_user_name()}! What would you like to do?\n1. Play a new game\n2. View the results of a previous game\n3. Quit")
        while True:
            user_input = input()
            if user_input.isnumeric():
                if user_input == "1":
                    print("one")
                elif input == "2":
                    print("two")
                elif input == "3":
                    raise KeyboardInterrupt
                else:
                    print("Please select 1, 2 or 3")
                    pass
    except KeyboardInterrupt:
        clear_terminal()
        print("It was fun while it lasted. See you next time!")

main_menu()

import os
from time import sleep
from main_menu import *

print("Welcome to the Guessing Game.\nYou will be asked a series of trivia questions that relate to different decades and years from the last 100 years. Answer the questions correctly with relation to your year of birth to see if we can guess your age correctly.\nPress ENTER to continue.")

if input() == "":
    if os.name == 'posix':
        os.system('clear')
    elif not os.name == 'posix':
        os.system('cls')
    else:
        sleep(10)

get_user_name()
main_menu()

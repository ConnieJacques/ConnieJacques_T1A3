import os
from time import sleep
from questions import *
from save_results import *
from clear import clear
from menu import main_menu 

clear()
print("Welcome to the Quiz Game.\nYou will be asked a series of trivia questions that relate to different decades and years from the last 100 years. Answer the questions correctly with relation to your year of birth to see if we can guess your age correctly.\nPress ENTER to continue.")

if input() == "":
    clear()
else:
    sleep(5)

main_menu()



import os
import user_results
from clear import clear
import pyinputplus as pyip
import questions



# Get and validate user's name
def get_user_name():
    print("To begin, please enter your name:")
    try:
        # Prompt user to enter their name until input contains only letters of the alphabet.
        while True:
            user_name = input()
            if not user_name.isalpha():
                    print("Please enter your name:")
                    continue
            # Terminate program if user enters 'quit'
            elif user_name.lower() == 'quit':
                raise KeyboardInterrupt
            else:
                # Accept answer and add to user_results list for later access
                name = "Name: "
                user_results.user_answer_list.append(name)
                user_results.user_answer_list.append(user_name)
                return user_name        
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit

def main_menu():
    print(f"Hi {get_user_name()}! What would you like to do?\n1. Play a new game\n2. View the results of a previous game\n3. Quit")
    try:
        user_input = pyip.inputChoice(['1', '2', '3', 'QUIT'])
        if user_input == '1':
            questions.question_one_answers()
            clear()
            questions.question_three_answers(questions.question_two_answers())
            clear()
            questions.question_five_answers(questions.question_four_answers())
            clear()
            questions.results()
            print("Press ENTER to continue")
            cont = input("")
            break
        elif user_input == '2':
            # view previous results
            pass
        elif user_input == '3' or user_input == 'quit':
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit

main_menu()
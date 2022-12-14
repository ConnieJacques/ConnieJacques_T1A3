import datetime
import facts
import randfacts
from dateutil.relativedelta import relativedelta as rd
from clear import clear
import pyinputplus as pyip
import user_results
import questions


# Ask user for the month they were born in
def get_month():
    print("In what month were you born? Please enter a number between 1 - 12")
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif user_input in range(1, 12 + 1):
            return user_input
        else:
            user_input = pyip.inputInt(min = 1, max = 12)
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# Ask user for the day they were born on
def get_day():
    print("On what day of the month were you born? Please enter a number between 1 - 31")
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif user_input in range(1, 31 + 1):
            return user_input
        else: 
            user_input = pyip.inputInt(min = 1, max = 31)
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


def results():
    # Prompt user for month of birth and store in variable month
    month = get_month()
    # clear()
    # Prompt user for day of birth and store in variable day
    day = get_day()
    # Get today's date
    today = datetime.date.today()
    # get datetime object dfor users birthday
    birthday = datetime.date(1991, month, day)
    # Calculate user's age
    age_year = rd(today, birthday)
    # Display result and append to results list global variable
    your_age = print(f"You are {age_year.years} years old!")
    user_results.user_answer_list.append(age_year.years)
    # Display custom fact for user and append to results list
    custom_fact = print(f"Fun fact for the year {1991}: {facts.dictionary.get(('1991'))}")
    user_results.user_answer_list.append(custom_fact)
    # Get bonus random fact and append to results list
    random_fact = randfacts.get_fact()
    display_random_fact = print(f"BONUS! enjoy this fun, completely random fact:\n{random_fact}")
    user_results.user_answer_list.append(display_random_fact)

# clear()
results()

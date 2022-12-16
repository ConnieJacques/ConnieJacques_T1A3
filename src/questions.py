import pyinputplus as pyip
import csv
from clear import clear
import user_results
import datetime
import facts
import randfacts
from dateutil.relativedelta import relativedelta as rd



# Dictionary contains key = question number, values = question
questions_dictionary = {
    'Question One:': 'Which generation do you belong to?',
    'Question Two:': 'Which popular novel was released in the decade you were born?',
    'Question Three:': 'Who was the Prime Minister of Australia in the year you were born?',
    'Question Four:': 'Which musicians and bands were popular in the year you were born?',
    'Question Five:': 'What was the highest grossing film in the year you were born?'
}


# Questions class to make a framework for asking the questions
class Questions:
    def __init__(self, number, question):
        self.number = number 
        self.question = question

# Class instances to store and format the questions
question_one = Questions(((list(questions_dictionary.keys())[0])), (list(questions_dictionary.values())[0]))
question_two = Questions(((list(questions_dictionary.keys())[1])), (list(questions_dictionary.values())[1]))
question_three = Questions(((list(questions_dictionary.keys())[2])), (list(questions_dictionary.values())[2]))
question_four = Questions(((list(questions_dictionary.keys())[3])), (list(questions_dictionary.values())[3]))
question_five = Questions(((list(questions_dictionary.keys())[4])), (list(questions_dictionary.values())[4]))


# Access question.csv to read the answer options and store these in a list so they can be accessed via their indexes
with open('question.csv') as f:
    reader = csv.DictReader(f)
    possible_answers = []
    for row in reader:
        possible_answers.append(row['answer_value'])

#  Access questions.csv to save row answers to question five to a list
with open('question.csv') as f:
    reader = csv.DictReader(f)
    years = []
    for row in reader:
        years.append(row['year_range'])



# Prints alternating answer codes and possible answers to format the answers
    def question_series(question_code, question, answer_options):
        # List contains answer codes
        question_values = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)']
        print(question_code, question)
        for i, j in (zip(question_values, answer_options)):
            print(i, j)


# assess user answer is between letters a - g
def answer_actions_ag():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abcdefg':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c', 'd', 'e', 'f', 'g'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# assess user's answer is between letters a - k
def answer_actions_ak():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abcdefghijk':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# assess user answer is between letters a - c
def answer_actions_ac():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abc':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# assess user answer is between letters a - d
def answer_actions_ad():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abcd':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c', 'd'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# assess user answer is between letters a - e
def answer_actions_ae():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abcde':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c', 'd', 'e'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# assess user answer is between letters a - f
def answer_actions_af():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abcdef':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c', 'd', 'e', 'f'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# assess user answer is between letters a - h
def answer_actions_ah():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abcdefgh':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c', 'd', 'e', 'f', 'g', 'h'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


# assess user's answer is between letters a - j
def answer_actions_aj():
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(user_input) == 1 and user_input.lower() in 'abcdefghij':
            return user_input
        else: 
            user_input = pyip.inputChoice(['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
            return user_input
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit
     

# First question and first set of possible answers
def question_one_answers():
    try:
    # Directions for the user
        print("Please answer questions by typing the corresponding letter and pressing ENTER\nEnd the program without saving by typing QUIT and pressing ENTER")
        (question_series(question_one.number, question_one.question, possible_answers[:7]))
        answer_option = answer_actions_ag()
        user_results.user_answer_list.append(question_one.number)
        if answer_option == 'a':
            user_results.user_answer_list.append(possible_answers[0])
        elif answer_option == 'b':
            user_results.user_answer_list.append(possible_answers[1])
        elif answer_option == 'c':
            user_results.user_answer_list.append(possible_answers[2])
        elif answer_option == 'd':
            user_results.user_answer_list.append(possible_answers[3])
        elif answer_option == 'c':
            user_results.user_answer_list.append(possible_answers[4])
        elif answer_option == 'd':
            user_results.user_answer_list.append(possible_answers[5])
        elif answer_option == 'e':
            user_results.user_answer_list.append(possible_answers[6])
        elif answer_option == 'f':
            user_results.user_answer_list.append(possible_answers[7])
        elif answer_option == 'g':
            user_results.user_answer_list.append(possible_answers[8])
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")
        raise SystemExit


# Second question and possible answers >> question 3 has become question 2
def question_two_answers():
    user_results.user_answer_list.append(question_two.number)
    try: 
        (question_series(question_two.number, question_two.question, possible_answers[18:29]))
        answer_option = answer_actions_ak()
        if answer_option == 'a':
            user_results.user_answer_list.append(possible_answers[18])
        elif answer_option == 'b':
            user_results.user_answer_list.append(possible_answers[19])
        elif answer_option == 'c':
            user_results.user_answer_list.append(possible_answers[20])
        elif answer_option == 'd':
            user_results.user_answer_list.append(possible_answers[21])
        elif answer_option == 'c':
            user_results.user_answer_list.append(possible_answers[22])
        elif answer_option == 'd':
            user_results.user_answer_list.append(possible_answers[23])
        elif answer_option == 'e':
            user_results.user_answer_list.append(possible_answers[24])
        elif answer_option == 'f':
            user_results.user_answer_list.append(possible_answers[25])
        elif answer_option == 'g':
            user_results.user_answer_list.append(possible_answers[26])
        elif answer_option == 'h':
            user_results.user_answer_list.append(possible_answers[27])
        elif answer_option == 'i':
            user_results.user_answer_list.append(possible_answers[28])
        elif answer_option == 'j':
            user_results.user_answer_list.append(possible_answers[29])
        elif answer_option == 'k':
            user_results.user_answer_list.append(possible_answers[30])
        clear()
        return answer_option
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")
        raise SystemExit

# Question three and possible answers
def question_three_answers(qtwo):
    user_results.user_answer_list.append(question_three.number)
    match qtwo:
        case 'a':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[29:32]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[29])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[30])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[31])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'b':
            try: 
                (question_series(question_three.number, question_three.question, possible_answers[31:35]))
                answer_option = answer_actions_ad()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[31])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[32])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[33])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[34])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'c':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[35:40]))
                answer_option = answer_actions_ae()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[35])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[36])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[37])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[38])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[39])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'd':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[39:42]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[39])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[40])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[41])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'e':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[39:43]))
                answer_option = answer_actions_ad()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[39])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[40])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[41])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[42])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'f':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[42:46]))
                answer_option = answer_actions_ad()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[42])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[43])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[44])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[45])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'g':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[44:47]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[44])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[45])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[46])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'h':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[46:49]))
                answer_actions_ac()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[46])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[47])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[48])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'i':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[48:51]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[48])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[49])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[50])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'j':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[50:56]))
                answer_option = answer_actions_af()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[50])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[51])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[52])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[53])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[54])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[55])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'k':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[53:56]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[53])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[54])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[55])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
                raise SystemExit


# Fourth question and possible answers
def question_four_answers():
    try: 
        (question_series(question_four.number, question_four.question, possible_answers[7:18]))
        answer_option = answer_actions_ak()
        user_results.user_answer_list.append(question_four.number)
        if answer_option == 'a':
            user_results.user_answer_list.append(possible_answers[7])
        elif answer_option == 'b':
            user_results.user_answer_list.append(possible_answers[8])
        elif answer_option == 'c':
            user_results.user_answer_list.append(possible_answers[9])
        elif answer_option == 'd':
            user_results.user_answer_list.append(possible_answers[10])
        elif answer_option == 'c':
            user_results.user_answer_list.append(possible_answers[11])
        elif answer_option == 'd':
            user_results.user_answer_list.append(possible_answers[12])
        elif answer_option == 'e':
            user_results.user_answer_list.append(possible_answers[13])
        elif answer_option == 'f':
            user_results.user_answer_list.append(possible_answers[14])
        elif answer_option == 'g':
            user_results.user_answer_list.append(possible_answers[15])
        elif answer_option == 'h':
            user_results.user_answer_list.append(possible_answers[16])
        elif answer_option == 'i':
            user_results.user_answer_list.append(possible_answers[17])
        elif answer_option == 'j':
            user_results.user_answer_list.append(possible_answers[18])
        elif answer_option == 'k':
            user_results.user_answer_list.append(possible_answers[19])
        clear()   
        return answer_option
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")
        raise SystemExit


# Question five - prints answer options based on the input taken in response to question_three_answers()
def question_five_answers(qfour):
    user_results.user_answer_list.append(question_five.number)
    match qfour:
        case 'a':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[56:64]))
                answer_option = answer_actions_ah()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[56])
                    user_results.birth_year.append(years[56])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[57])
                    user_results.birth_year.append(years[57])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[58])
                    user_results.birth_year.append(years[58])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[59])
                    user_results.birth_year.append(years[59])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[60])
                    user_results.birth_year.append(years[60])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[61])
                    user_results.birth_year.append(years[61])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[62])
                    user_results.birth_year.append(years[62])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[63])
                    user_results.birth_year.append(years[63])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'b':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[64:74]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[64])
                    user_results.birth_year.append(years[64])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[65])
                    user_results.birth_year.append(years[65])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[66])
                    user_results.birth_year.append(years[66])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[67])
                    user_results.birth_year.append(years[67])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[68])
                    user_results.birth_year.append(years[68])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[69])
                    user_results.birth_year.append(years[69])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[70])
                    user_results.birth_year.append(years[70])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[71])
                    user_results.birth_year.append(years[71])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[72])
                    user_results.birth_year.append(years[72])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[73])
                    user_results.birth_year.append(years[73])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'c':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[74:84]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[74])
                    user_results.birth_year.append(years[74])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[75])
                    user_results.birth_year.append(years[75])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[76])
                    user_results.birth_year.append(years[76])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[77])
                    user_results.birth_year.append(years[77])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[78])
                    user_results.birth_year.append(years[78])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[79])
                    user_results.birth_year.append(years[79])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[80])
                    user_results.birth_year.append(years[80])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[81])
                    user_results.birth_year.append(years[81])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[82])
                    user_results.birth_year.append(years[82])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[83])
                    user_results.birth_year.append(years[83])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'd':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[84:94]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[84])
                    user_results.birth_year.append(years[84])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[85])
                    user_results.birth_year.append(years[85])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[86])
                    user_results.birth_year.append(years[86])
                if answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[87])
                    user_results.birth_year.append(years[87])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[88])
                    user_results.birth_year.append(years[88])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[89])
                    user_results.birth_year.append(years[89])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[90])
                    user_results.birth_year.append(years[90])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[91])
                    user_results.birth_year.append(years[91])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[92])
                    user_results.birth_year.append(years[92])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[93])
                    user_results.birth_year.append(years[93])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'e':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[94:104]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[94])
                    user_results.birth_year.append(years[94])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[95])
                    user_results.birth_year.append(years[95])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[96])
                    user_results.birth_year.append(years[96])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[97])
                    user_results.birth_year.append(years[97])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[98])
                    user_results.birth_year.append(years[98])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[99])
                    user_results.birth_year.append(years[99])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[100])
                    user_results.birth_year.append(years[100])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[101])
                    user_results.birth_year.append(years[101])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[102])
                    user_results.birth_year.append(years[102])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[103])
                    user_results.birth_year.append(years[103])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case'f':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[104:114]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[104])
                    user_results.birth_year.append(years[104])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[105])
                    user_results.birth_year.append(years[105])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[106])
                    user_results.birth_year.append(years[106])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[107])
                    user_results.birth_year.append(years[107])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[108])
                    user_results.birth_year.append(years[108])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[109])
                    user_results.birth_year.append(years[109])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[110])
                    user_results.birth_year.append(years[110])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[111])
                    user_results.birth_year.append(years[111])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[112])
                    user_results.birth_year.append(years[112])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[113])
                    user_results.birth_year.append(years[113])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'g':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[114:124]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[114])
                    user_results.birth_year.append(years[114])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[115])
                    user_results.birth_year.append(years[115])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[116])
                    user_results.birth_year.append(years[116])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[117])
                    user_results.birth_year.append(years[117])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[118])
                    user_results.birth_year.append(years[118])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[119])
                    user_results.birth_year.append(years[119])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[120])
                    user_results.birth_year.append(years[120])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[121])
                    user_results.birth_year.append(years[121])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[122])
                    user_results.birth_year.append(years[122])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[123])
                    user_results.birth_year.append(years[123])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'h':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[124:134]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[124])
                    user_results.birth_year.append(years[124])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[125])
                    user_results.birth_year.append(years[125])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[126])
                    user_results.birth_year.append(years[126])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[127])
                    user_results.birth_year.append(years[127])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[128])
                    user_results.birth_year.append(years[128])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[129])
                    user_results.birth_year.append(years[129])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[130])
                    user_results.birth_year.append(years[130])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[131])
                    user_results.birth_year.append(years[131])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[132])
                    user_results.birth_year.append(years[132])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[133])
                    user_results.birth_year.append(years[133])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'i':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[134:144]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[134])
                    user_results.birth_year.append(years[134])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[135])
                    user_results.birth_year.append(years[135])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[136])
                    user_results.birth_year.append(years[136])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[137])
                    user_results.birth_year.append(years[137])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[138])
                    user_results.birth_year.append(years[138])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[139])
                    user_results.birth_year.append(years[139])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[140])
                    user_results.birth_year.append(years[140])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[141])
                    user_results.birth_year.append(years[141])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[142])
                    user_results.birth_year.append(years[142])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[143])
                    user_results.birth_year.append(years[143])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'j':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[144:154]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[144])
                    user_results.birth_year.append(years[144])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[145])
                    user_results.birth_year.append(years[145])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[146])
                    user_results.birth_year.append(years[146])
                elif answer_option == 'd':
                    user_results.user_answer_list.append(possible_answers[147])
                    user_results.birth_year.append(years[147])
                elif answer_option == 'e':
                    user_results.user_answer_list.append(possible_answers[148])
                    user_results.birth_year.append(years[148])
                elif answer_option == 'f':
                    user_results.user_answer_list.append(possible_answers[149])
                    user_results.birth_year.append(years[149])
                elif answer_option == 'g':
                    user_results.user_answer_list.append(possible_answers[150])
                    user_results.birth_year.append(years[150])
                elif answer_option == 'h':
                    user_results.user_answer_list.append(possible_answers[151])
                    user_results.birth_year.append(years[151])
                elif answer_option == 'i':
                    user_results.user_answer_list.append(possible_answers[152])
                    user_results.birth_year.append(years[152])
                elif answer_option == 'j':
                    user_results.user_answer_list.append(possible_answers[153])
                    user_results.birth_year.append(years[153])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'k':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[154:157]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_results.user_answer_list.append(possible_answers[154])
                    user_results.birth_year.append(years[154])
                elif answer_option == 'b':
                    user_results.user_answer_list.append(possible_answers[155])
                    user_results.birth_year.append(years[155])
                elif answer_option == 'c':
                    user_results.user_answer_list.append(possible_answers[156])
                    user_results.birth_year.append(years[156])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
                raise SystemExit



# Ask user for the month they were born in
def get_month():
    print("In what month were you born? Please enter a number between 1 - 12")
    user_input = input()
    try:
        if user_input.lower() == 'quit':
            raise KeyboardInterrupt
        user_input = int(user_input)
        if user_input in range(1, 12 + 1):
            clear()
            return user_input
        else:
            user_input = pyip.inputInt(prompt = "Please enter a number between 1 - 12\n", min = 1, max = 12)
            clear()
            return user_input
    except ValueError:
        pyip.inputInt(prompt = "Please enter a number between 1 - 12\n", min = 1, max = 12)
        clear()        
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
        user_input = int(user_input)
        if user_input in range(1, 31 + 1):
            clear()
            return user_input
        else:
            user_input = pyip.inputInt(prompt = "Please enter a number between 1 - 31\n", min = 1, max = 31)
            clear()
            return user_input
    except ValueError:
        pyip.inputInt(prompt = "Please enter a number between 1 - 31\n", min = 1, max = 31)
        clear()  
    except ValueError:
        pyip.inputInt(prompt = "Please enter a number between 1 - 12\n", min = 1, max = 12)
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit


def results():
    clear()
    # Prompt user for month of birth and store in variable month
    month = get_month()
    # clear()
    # Prompt user for day of birth and store in variable day
    day = get_day()
    # Get today's date
    today = datetime.date.today()
    # get datetime object dfor users birthday
    birthday_year = user_results.birth_year[0]
    birthday = datetime.date(int(birthday_year), int(month), int(day))
    # Calculate user's age
    age_year = rd(today, birthday)
    # Display result and append to results list global variable
    print(f"You are {age_year.years} years old!\n")
    age = "Age: "
    str_years = str(age_year.years)
    user_results.user_answer_list.append(age)
    user_results.user_answer_list.append(str_years)
    # Display custom fact for user and append to results list
    print(f"Fun fact for the year {user_results.birth_year[0]}:\n{facts.dictionary.get(int(birthday_year))}")
    user_results.user_answer_list.append(facts.dictionary.get(int(birthday_year)))
    # Get bonus random fact and append to results list
    random_fact = randfacts.get_fact()
    print(f"BONUS! enjoy this fun, completely random fact:\n{random_fact}")
    return age_year
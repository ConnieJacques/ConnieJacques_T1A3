import pyinputplus as pyip
import csv
from clear import clear


questions_dictionary = {
    'Question One:': 'Which generation do you belong to?',
    'Question Two:': 'Which popular novel was released in the decade you were born?',
    'Question Three:': 'Who was the Prime Minister of Australia in the year you were born?',
    'Question Four:': 'Which musicians and bands were popular in the year you were born?',
    'Question Five:': 'What was the highest grossing film in the year you were born?'
}



# Questions class is framework for questions
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


# Access question.csv to read the questions and store in a list so they can be accessed via their indexes
with open('question.csv') as f:
    reader = csv.DictReader(f)
    possible_answers = []
    for row in reader:
        possible_answers.append(row['answer_value'])

# List contains answer codes
question_values = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)', 'n)', 'o)', 'p)', 'q)', 'r)', 's)', 't)']


def question_series(question_code, question, answer_options):
    # Ask the first question
    print(question_code, question)
    # Prints alternating answer codes and possible answers to format the answers
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
     

# First question and first set of possible answers
def question_one_answers():
    try:
    # Directions for the user
        print("Please answer questions by typing the corresponding letter and pressing ENTER\nEnd the program without saving by typing QUIT and pressing ENTER")
        (question_series(question_one.number, question_one.question, possible_answers[:7]))
        answer_actions_ag()
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")


# Second question and possible answers >> question 3 has become question 2
def question_two_answers():
    try: 
        (question_series(question_two.number, question_two.question, possible_answers[18:29]))
        answer = answer_actions_ak()
        return answer
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")

# Question three and possible answers
def question_three_answers():
    match possible_user_answers:
        case 'a':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[29:32]))
                answer_actions_ac()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'b':
            try: 
                (question_series(question_three.number, question_three.question, possible_answers[31:35]))
                answer_actions_ad()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'c':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[35:40]))
                answer_actions_ae()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'd':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[39:42]))
                answer_actions_ac()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'e':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[39:43]))
                answer_actions_ad()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'f':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[42:46]))
                answer_actions_ad()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'g':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[44:47]))
                answer_actions_ac()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'h':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[46:49]))
                answer_actions_ac()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'i':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[48:51]))
                answer_actions_ac()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'j':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[50:56]))
                answer_actions_af()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'k':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[53:56]))
                answer_actions_ac()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")


# Fourth question and possible answers
def question_four_answers():
    try: 
        (question_series(question_four.number, question_four.question, possible_answers[7:18]))
        answer = answer_actions_ak()
        return answer
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")


# Question five - prints answer options based on the input taken in response to question_three_answers()
def question_five_answers():
    match possible_user_answers:
        case 'a':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[56:64]))
                answer_actions_ah()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'b':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[64:74]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'c':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[74:84]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'd':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[84:94]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'e':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[94:104]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case'f':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[104:114]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'g':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[114:124]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'h':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[124:134]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'i':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[134:144]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'j':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[144:154]))
                answer_actions_aj()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'k':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[154:157]))
                answer_actions_ac()
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")

# Clear terminal 
clear()

# Ask first queestion
question_one_answers()
clear()

# Ask second question
possible_user_answers = question_two_answers()
clear()

# Ask third question
question_three_answers()
clear()

# Ask fourth question
possible_user_answers = question_four_answers()
clear()

# Ask firth question
question_five_answers()
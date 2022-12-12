import csv

# import pyinputplus
# inputChoice() Ensures the user enters one of the provided choices

# Dictionary stores the quizz game's questions
questions_dictionary = {
    'Question One:': 'Which generation do you belong to?',
    'Question Two:': 'Which musicians and bands were popular in the year you were born?',
    'Question Four:': 'Which popular novel was released in the decade you were born?',
    'Question Three:': 'Who was the Prime Minister of Australia in the year you were born?',
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


# assess user answer
def answer_actions():
    user_input = input()
    # try:
    if len(user_input) == 1 and user_input.lower().isalpha():
        return user_input
        # else:
        #     print("Please answer questions by entering the corresponding letter and pressing ENTER.")
    # except user_input == "quit":
    #     raise KeyboardInterrupt
     

# First question and first set of possible answers
def question_one_answers():
    # Directions for the user
    print("Please answer questions by entering the corresponding letter and pressing ENTER.")
    (question_series(question_one.number, question_one.question, possible_answers[:7]))
    # user_answer = answer_actions()
    # return answer_actions

# Second question and possible answers
def question_two_answers():
    if answer_actions() in "abcdefghijk":
        (question_series(question_two.number, question_two.question, possible_answers[7:18]))
        return answer_actions


# Third questions and possible answers
def question_three_answers():
    if answer_actions() in "abcdefghijk":
    # Third question and possible answers
        (question_series(question_three.number, question_three.question, possible_answers[18:29]))
        return answer_actions()

# Question four and possible answers
def question_four_answers():
    match answer_actions():
        case 'a':
            (question_series(question_four.number, question_four.question, possible_answers[29:32]))
            return 'a'
        case 'b':
            (question_series(question_four.number, question_four.question, possible_answers[31:35]))
            return 'b'
        case 'c':
            (question_series(question_four.number, question_four.question, possible_answers[35:40]))
            return 'c'
        case 'd':
            (question_series(question_four.number, question_four.question, possible_answers[39:42]))
            return 'd'
        case 'e':
            (question_series(question_four.number, question_four.question, possible_answers[39:43]))
            return 'e'
        case 'f':
            (question_series(question_four.number, question_four.question, possible_answers[42:46]))
            return 'f'
        case 'g':
            (question_series(question_four.number, question_four.question, possible_answers[44:47]))
            return 'g'
        case 'h':
            (question_series(question_four.number, question_four.question, possible_answers[46:49]))
            return 'h'
        case 'i':
            (question_series(question_four.number, question_four.question, possible_answers[48:51]))
            return 'i'
        case 'j':
            (question_series(question_four.number, question_four.question, possible_answers[50:56]))
            return 'j'
        case 'k':
            (question_series(question_four.number, question_four.question, possible_answers[53:56]))
            return 'k'


# Question five - prints answer options based on the input taken in response to question_three_answers()
def question_five_answers():
    match question_three_answers():
        case 'a':
            (question_series(question_five.number, question_five.question, possible_answers[56:64]))
        case 'b':
            (question_series(question_five.number, question_five.question, possible_answers[64:74]))
        case 'c':
            (question_series(question_five.number, question_five.question, possible_answers[74:84]))
        case 'd':
            (question_series(question_five.number, question_five.question, possible_answers[84:94]))
        case 'e':
            (question_series(question_five.number, question_five.question, possible_answers[94:104]))
        case'f':
            (question_series(question_five.number, question_five.question, possible_answers[104:114]))
        case 'g':
            (question_series(question_five.number, question_five.question, possible_answers[114:124]))
        case 'h':
            (question_series(question_five.number, question_five.question, possible_answers[124:134]))
        case 'i':
            (question_series(question_five.number, question_five.question, possible_answers[134:144]))
        case 'j':
            (question_series(question_five.number, question_five.question, possible_answers[144:154]))
        case 'k':
            (question_series(question_five.number, question_five.question, possible_answers[154:157]))


question_one_answers()

question_two_answers()

# question_three_answers()

question_four_answers()

question_five_answers()
answer_actions()



# with open('question.csv') as f:
#         reader = csv.DictReader(f)
#         birth_year = []
#         for row in reader:
#             birth_year.append(row['year_range'])






# print(question_four.question)
 
# def ask_user_questions():


# def question_one():
#     # answer = input()
#     for key in questions_dictionary.items():
#         print(key)
        
        
    # while answer != "quit":

# question_one()
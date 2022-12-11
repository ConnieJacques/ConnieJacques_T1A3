from itertools import chain
import csv

# import pyinputplus
# inputChoice() Ensures the user enters one of the provided choices

# Dictionary stores the quizz game's questions
questions_dictionary = {
    'Question One:': 'Which generation do you belong to?',
    'Questions Two:': 'Which musicians and bands were popular in the year you were born?',
    'Questions Three:': 'Which popular novel was released in the decade you were born?',
    'Questions Four:': 'Who was the Prime Minister of Australia in the year you were born?',
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
question_values = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)']

# Directions for the user
print("Please answer questions by entering the corresponding letter and pressing ENTER.")

def question_series(question_code, question, answer_options):
    # Ask the first question
    print(question_code, question)
    # Prints alternating answer codes and possible answers to format the answers
    for i, j in (zip(question_values, answer_options)):
        print(i, j)


# First question and first set of possible answers
(question_series(question_one.number, question_one.question, possible_answers[:7]))

# # Ask the first question
# print(question_one.number, question_one.question)
# # Prints alternating answer codes and possible answers to format the answers
# for i, j in (zip(question_values, possible_answers[:7])):
#     print(i, j)


# assess user answer
def answer_actions():
    user_input = input()
    if len(user_input) == 1 and user_input.lower().isalpha():
        return user_input
    else:
        print("Please answer questions by entering the corresponding letter and pressing ENTER.")

# question two
match answer_actions():
    case 'a':
        (question_series(question_two.number, question_two.question, possible_answers[14:18]))
    case 'b':
        (question_series(question_two.number, question_two.question, possible_answers[14:18]))
    case 'c':
        (question_series(question_two.number, question_two.question, possible_answers[11:15]))
    case 'd':
        (question_series(question_two.number, question_two.question, possible_answers[11:15]))
    case 'e':
        (question_series(question_two.number, question_two.question, possible_answers[7:12]))
    case 'f':
        (question_series(question_two.number, question_two.question, possible_answers[7:12]))
    case 'g':
        (question_series(question_two.number, question_two.question, possible_answers[7:12]))

# question three
match answer_actions():
    case 'a':
        (question_series(question_three.number, question_three.question, possible_answers[14:18]))
    case 'b':
        (question_series(question_three.number, question_three.question, possible_answers[14:18]))
    case 'c':
        (question_series(question_three.number, question_three.question, possible_answers[11:15]))
    case 'd':
        (question_series(question_three.number, question_three.question, possible_answers[11:15]))
    case 'e':
        (question_series(question_three.number, question_three.question, possible_answers[7:12]))
    case 'f':
        (question_series(question_three.number, question_three.question, possible_answers[7:12]))
    case 'g':
        (question_series(question_three.number, question_three.question, possible_answers[7:12]))

# Returns new list of alternating answer codes and possible answers to format the answers
# for i, j in (zip(question_values, possible_answers[:7])):
#     print(i, j)

# def q_one():
#     print(f"{question_one.number} {question_one.question}")
#     user_input = input()
#     user_input = user_input.lower()
#     match user_input:
#         case 'a':





# print(question_four.question)
 
# def ask_user_questions():


# def question_one():
#     # answer = input()
#     for key in questions_dictionary.items():
#         print(key)
        
        
    # while answer != "quit":

# question_one()
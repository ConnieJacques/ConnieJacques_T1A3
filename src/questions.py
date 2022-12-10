# import pyinputplus
# inputChoice() Ensures the user enters one of the provided choices

questions_dictionary = {
    'Question One:': 'Which generation do you belong to?',
    'Questions Two:': 'Which musicians and bands were popular in the year you were born?',
    'Questions Three:': 'Which popular novel was released in the decade you were born?',
    'Questions Four:': 'Who was the Prime Minister of Australia in the year you were born?',
    'Question Five:': 'What was the highest grossing film in the year you were born?'
}

class Questions:
    def __init__(self, number, question):
        self.number = number 
        self.question = question

question_one = Questions(((list(questions_dictionary.keys())[0])), (list(questions_dictionary.values())[0]))
question_two = Questions(((list(questions_dictionary.keys())[1])), (list(questions_dictionary.values())[1]))
question_three = Questions(((list(questions_dictionary.keys())[2])), (list(questions_dictionary.values())[2]))
question_four = Questions(((list(questions_dictionary.keys())[3])), (list(questions_dictionary.values())[3]))
question_five = Questions(((list(questions_dictionary.keys())[4])), (list(questions_dictionary.values())[4]))

print(question_four.question)
 
def ask_user_questions():


# def question_one():
#     # answer = input()
#     for key in questions_dictionary.items():
#         print(key)
        
        
    # while answer != "quit":

# question_one()

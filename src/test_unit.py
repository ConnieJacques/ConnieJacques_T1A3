# test correctly extracting data from facts_dictionary.txt file and storing as a dictionary key == date value == the correlating fact
dictionary = {}
with open('facts_dictionary.txt') as f:
    for line in f:
        key = line[:4]
        val = line[5:]
        dictionary[int(key)] = val

# check all expected keys available
assert 1922 in dictionary.keys()
assert 1999 in dictionary.keys()
assert 2022 in dictionary.keys()

# check values match
assert "The classic German vampire movie" in dictionary[1922]


# check Questions class can access dictionaryclass Questions:
questions_dictionary = {
    'Question One:': 'Which generation do you belong to?'}

class Questions:
    def __init__(self, number, question):
        self.number = number 
        self.question = question

question_one = Questions(((list(questions_dictionary.keys())[0])), (list(questions_dictionary.values())[0]))

assert question_one.number == "Question One:"
assert "Which" in question_one.question
import pyinputplus as pyip
import csv
from clear import clear


# List contains the users answers so they are available to be written to a file and viewed later
user_answer_list = []


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
        answer_option = answer_actions_ag()
        user_answer_list.append(question_one.number)
        if answer_option == 'a':
            user_answer_list.append(possible_answers[0])
        if answer_option == 'b':
            user_answer_list.append(possible_answers[1])
        if answer_option == 'c':
            user_answer_list.append(possible_answers[2])
        if answer_option == 'd':
            user_answer_list.append(possible_answers[3])
        if answer_option == 'c':
            user_answer_list.append(possible_answers[4])
        if answer_option == 'd':
            user_answer_list.append(possible_answers[5])
        if answer_option == 'e':
            user_answer_list.append(possible_answers[6])
        if answer_option == 'f':
            user_answer_list.append(possible_answers[7])
        if answer_option == 'g':
            user_answer_list.append(possible_answers[8])
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")


# Second question and possible answers >> question 3 has become question 2
def question_two_answers():
    user_answer_list.append(question_two.number)
    try: 
        (question_series(question_two.number, question_two.question, possible_answers[18:29]))
        answer_option = answer_actions_ak()
        if answer_option == 'a':
            user_answer_list.append(possible_answers[18])
        if answer_option == 'b':
            user_answer_list.append(possible_answers[19])
        if answer_option == 'c':
            user_answer_list.append(possible_answers[20])
        if answer_option == 'd':
            user_answer_list.append(possible_answers[21])
        if answer_option == 'c':
            user_answer_list.append(possible_answers[22])
        if answer_option == 'd':
            user_answer_list.append(possible_answers[23])
        if answer_option == 'e':
            user_answer_list.append(possible_answers[24])
        if answer_option == 'f':
            user_answer_list.append(possible_answers[25])
        if answer_option == 'g':
            user_answer_list.append(possible_answers[26])
        if answer_option == 'h':
            user_answer_list.append(possible_answers[27])
        if answer_option == 'i':
            user_answer_list.append(possible_answers[28])
        if answer_option == 'j':
            user_answer_list.append(possible_answers[29])
        if answer_option == 'k':
            user_answer_list.append(possible_answers[30])
        return answer_option
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")

# Question three and possible answers
def question_three_answers():
    user_answer_list.append(question_three.number)
    match possible_user_answers:
        case 'a':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[29:32]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[29])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[30])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[31])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'b':
            try: 
                (question_series(question_three.number, question_three.question, possible_answers[31:35]))
                answer_option = answer_actions_ad()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[31])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[32])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[33])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[34])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'c':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[35:40]))
                answer_option = answer_actions_ae()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[35])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[36])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[37])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[38])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[39])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'd':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[39:42]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                        user_answer_list.append(possible_answers[39])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[40])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[41])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'e':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[39:43]))
                answer_option = answer_actions_ad()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[39])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[40])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[41])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[42])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'f':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[42:46]))
                answer_option = answer_actions_ad()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[42])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[43])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[44])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[45])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'g':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[44:47]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[44])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[45])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[46])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'h':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[46:49]))
                answer_actions_ac()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[46])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[47])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[48])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'i':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[48:51]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[48])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[49])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[50])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'j':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[50:56]))
                answer_option = answer_actions_af()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[50])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[51])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[52])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[53])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[54])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[55])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'k':
            try:
                (question_series(question_three.number, question_three.question, possible_answers[53:56]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[53])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[54])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[55])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")


# Fourth question and possible answers
def question_four_answers():
    try: 
        (question_series(question_four.number, question_four.question, possible_answers[7:18]))
        answer_option = answer_actions_ak()
        user_answer_list.append(question_four.number)
        if answer_option == 'a':
            user_answer_list.append(possible_answers[7])
        if answer_option == 'b':
            user_answer_list.append(possible_answers[8])
        if answer_option == 'c':
            user_answer_list.append(possible_answers[9])
        if answer_option == 'd':
            user_answer_list.append(possible_answers[10])
        if answer_option == 'c':
            user_answer_list.append(possible_answers[11])
        if answer_option == 'd':
            user_answer_list.append(possible_answers[12])
        if answer_option == 'e':
            user_answer_list.append(possible_answers[13])
        if answer_option == 'f':
            user_answer_list.append(possible_answers[14])
        if answer_option == 'g':
            user_answer_list.append(possible_answers[15])
        if answer_option == 'h':
            user_answer_list.append(possible_answers[16])
        if answer_option == 'i':
            user_answer_list.append(possible_answers[17])
        if answer_option == 'j':
            user_answer_list.append(possible_answers[18])
        if answer_option == 'k':
            user_answer_list.append(possible_answers[19])
        return answer_option
    except KeyboardInterrupt:
        print("It was nice while it lasted! See you next time!")


# Question five - prints answer options based on the input taken in response to question_three_answers()
def question_five_answers():
    user_answer_list.append(question_five.number)
    match possible_user_answers:
        case 'a':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[56:64]))
                answer_option = answer_actions_ah()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[56])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[57])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[58])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[59])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[60])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[61])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[62])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[63])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'b':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[64:74]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[64])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[65])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[66])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[67])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[68])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[69])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[70])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[71])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[72])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[73])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'c':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[74:84]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[74])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[75])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[76])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[77])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[78])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[79])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[80])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[81])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[82])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[83])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'd':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[84:94]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[84])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[85])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[86])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[87])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[88])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[89])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[90])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[91])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[92])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[93])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'e':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[94:104]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[94])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[95])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[96])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[97])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[98])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[99])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[100])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[101])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[102])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[103])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case'f':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[104:114]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[104])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[105])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[106])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[107])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[108])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[109])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[110])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[111])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[112])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[113])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'g':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[114:124]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[114])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[115])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[116])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[117])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[118])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[119])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[120])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[121])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[122])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[123])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'h':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[124:134]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[124])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[125])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[126])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[127])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[128])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[129])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[130])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[131])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[132])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[133])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'i':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[134:144]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[134])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[135])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[136])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[137])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[138])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[139])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[140])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[141])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[142])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[143])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'j':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[144:154]))
                answer_option = answer_actions_aj()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[144])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[145])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[146])
                if answer_option == 'd':
                    user_answer_list.append(possible_answers[147])
                if answer_option == 'e':
                    user_answer_list.append(possible_answers[148])
                if answer_option == 'f':
                    user_answer_list.append(possible_answers[149])
                if answer_option == 'g':
                    user_answer_list.append(possible_answers[150])
                if answer_option == 'h':
                    user_answer_list.append(possible_answers[151])
                if answer_option == 'i':
                    user_answer_list.append(possible_answers[152])
                if answer_option == 'j':
                    user_answer_list.append(possible_answers[153])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")
        case 'k':
            try:
                (question_series(question_five.number, question_five.question, possible_answers[154:157]))
                answer_option = answer_actions_ac()
                if answer_option == 'a':
                    user_answer_list.append(possible_answers[154])
                if answer_option == 'b':
                    user_answer_list.append(possible_answers[155])
                if answer_option == 'c':
                    user_answer_list.append(possible_answers[156])
            except KeyboardInterrupt:
                print("It was nice while it lasted! See you next time!")

# Clear terminal 
clear()

# Ask first queestion
question_one_answers()
clear()

# # Ask second question
possible_user_answers = question_two_answers()
clear()

# # Ask third question
question_three_answers()
clear()


# # Ask fourth question
possible_user_answers = question_four_answers()
clear()

# # Ask firth question
question_five_answers()

print('\n'.join(user_answer_list))
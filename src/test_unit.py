import pytest

def dict():
    # Initialise empty dictionary
    dictionary = {}
    # Read from text file and save the first 4 characters of each line to the dictionary as keys, and the remained of the line to the dictionary as values
    with open('facts_dictionary.txt') as f:
        for line in f:
            key = line[:4]
            val = line[5:]
            dictionary[int(key)] = val

    return dictionary

# Test correctly extracting data from facts_dictionary.txt file and storing as a dictionary key == date value == the correlating fact
def test_dict():
    # Expect Pass
    assert 1922 in dict(), "Expect Pass, test passed as int 1922 is key in dicitonary"
    assert 2022 in dict(), "Expect Pass, test passed as int 2022 is key in dicitonary, confirms whole text file was added to dicitonary"
    assert "2022" in dict(), "Expect Fail, test passed as key for dictionary is integer, as expected"



# Test answer_actions_ac() function - function writen out here and not imported as user_input for specific value to be mocked for testing purposes
def answer_actions_ac(param):
    try:
        if param.lower() == 'quit':
            raise KeyboardInterrupt
        elif len(param) == 1 and param.lower() in 'abc':
            return param
    except KeyboardInterrupt:
        print("It was nice while it lasted. See you next time!")
        raise SystemExit

# Test input of "quit" triggers KeyboardInterupt to terminate program - expect Pass
def test_answer_actions_ac():
    with pytest.raises(SystemExit):
        answer_actions_ac("quit"), "Expect Pass, test passing as mocked input quit does produce SystemExit error" 





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
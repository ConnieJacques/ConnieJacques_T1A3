# extract data from 'facts_dictionary.txt' and stores it in a dictionary where key = date and value = correlating fact
dictionary = {}
with open('facts_dictionary.txt') as f:
    for line in f:
        key = line[:4]
        val = line[5:]
        dictionary[int(key)] = val



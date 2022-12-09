# integration testing to validate access to questions.csv and facts_dictionary.txt files

# test able to access facts_dictionary.txt file
def test_acess_txt_file():
   with open('facts_dictionary.txt') as f:
    query = f.read(4)
    assert int(query) == 1922


# check assess to question.csv file
import csv

def test_access_question_file():
    with open('question.csv') as f:
        reader = csv.DictReader(f)
        list =  []
        for row in reader:
            list.append(row['year_range'])
            
        assert '1981 - 1996' in list
        


    

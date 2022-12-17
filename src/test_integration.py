# integration testing to validate correctly accessing questions.csv file
import csv

def test_access_question_file():
    # Open csv file in read and assign each line as read into an empty list
    with open('question.csv') as f:
        reader = csv.DictReader(f)
        list =  []
        for row in reader:
            list.append(row['year_range'])
            
        assert '1981 - 1996' in list, "Expected Pass, test passed string is in the list and accessed as expected"
        assert '2024' not in list, "Expected, Pass, test passed because 2024 is not in list"
        assert 2022 in "list", "Expectecd Fail, test passing because int cannot be in the string, expected TypeError and produced TypeError"
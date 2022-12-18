# ConnieJacques_T1A3

## R4 - Repository Link

The source code for the Terminal App can be found here:
https://github.com/ConnieJacques/ConnieJacques_T1A3


## R5 - Identify any code style guide or styling conventions that the application will adhere to.

PEP 8 - Style Guide for Python Code was followed to dictate the coding conventions utilised in the writing of this command line application. Standards including, the use of four spaces per indentation level, surrounding top-level function definitions with two blank lines, placing imports on seperate lines, and recommendations for the placements of white spaces relative to braces and binary operators were followed throughout the project to promote readability and provide consistance to easier understanding of the code itself.

### Reference to the PEP 8 Style Guide:

van Rossum, Guido, Warsaw, Barry and Coghlan, Nick 2013, *PEP 8 – Style Guide for Python Code*, Python Enhancement Proposals, accessed at: https://peps.python.org/pep-0008/


## R6 - Develop a list of features that will be included in the application.

The features in my *Quiz Game* command line application are:

1. main_menu() - is the first major control structure as it is the main menu of the game that user returns to after each action and provides the user with a list of actions they can choose from. A while loop while loop continuiously prompts the user for input as it is set to True while prompting for input. There are four possible user actions available. 

This function utilises error handling with a try/except statement which allows the user to input the string "quit"or "4" to terminate the program by raising KeyboardInterupt with a custom exist message before raising SystemExit. Errors from user input are prevented by the use of the imported package *pyinputplus* which allows for the use of the mothod *pyip.inputChoice()*. This method prompts the user to provide input from a specified list of choices only and prompts the user to try again if their input is not in the list of choices. 

The first user option begins a new game of the *Quiz Game*. After the user recieved their results they are returned to the menu to choose their action. The second user option allows the user to save the results of their previous game. The thirds, allows them to see a list of game save game results and view a file of their choosing from these options. And, the last user menu option is to exit the program. If this choice is selected before the results are saved they will be lost.

2. get_user_name() - function prompts the user to input their name and appends the result to a global variable called user_answer_list. This variable was purposefully made global because it needs to be accessed in many locations throughout the app as it stores the user's answers to the questions they are asks. It needs to be accessable so that the contents of the list can be written into a text file to save the user's results for later viewing; the user's name as entered in this function is later used to name the text file where results are saved (if a file with the same name does not already exist). get_user_name() uses a while loop that runs while True to continuous ask the user to input their name. Input is checked to ensure it contains on letters using the .isalpha() method. If True, the input is appended to the list, if the input does not contain only letters the user is prompted to try again. This function utilises error handling with a try/except statement which allows the user to input the string "quit" to terminate the program by raising KeyboardInterupt with a custom exist message before raising SystemExit. 

3. Questions - a basic structure that takes two paramaters, one to provide the question number and the other the question. Instances of this class access dictionary where the key is the question number and the value is the actual question. This simple class method was choosen to allow for simplicity in accessing the contained infomation as both question keys and answer values are stored to the global variable user_answer_list and this was most straightforward way to access this infomation.

4. question_series(question_code, question, answer_options) - this function contains a list from a - k (the answer key for the possible answers provided for the user to select from) and zips (merges alternating indices from two lists) together the list of answer keys with answer options, that have previously been extracted from the question.csv file. 

5. clear() - a simple function that checks the user's operating system and clear the terminal to keep the application looking neat as it runs. The build-in package *os* is imported and used to check if the os is posix based or not and accord accordingly.

6. answer_action() functions - there are 6 similar small functions that take user input via the *pyip.inputChoice()* mothod and check the input is in a provided list that corresponds with the answer keys provided for the particular question that is being asked. Again, user input is checked for the string "quit" and will raise KeyboardInterupt and SystemExit errors to allow the user to eloquently terminate the program, if they wish to do so.

7. question_one_answers() - along with question_two_answers() and question_four_answers() functions provide the user with question by calling instances of the Question class to print the question, extract the possible answers from a list that was created by extracting a specific column from the questions.csv file and printing the possible corresponding possible answers by calling their indexes from the list. From there, an answer_action() function is called (which one depends on the number of possible answers that are provided for the user) and uses if/elif statements to append the user's inputed answer to the question to the global variable user_answer_list list of the user's answers from the game, before returning the corresponding input. Again, these functions call on an answer_action() function that handles user input as outsided in point 6. 

8. question_three_answers() and question_five_answers() - lengthy functions that respectively take the question_two_answers() and question_four_answers() functions are arguments. The functions are passed in so their returned values can be utilised as the answers to question_two_answers() and question_four_answers() determine what possible answers are provided for the user for questions question_three_answers() and question_five_answers(). The action to be taken is determined by a match case statement that that then breaks off into an if/elif/else statement to output the corresponding possible answer values for the user. The users answers is appened to the global variable user_answer_list list of the user's answers for the game. question_five _answers() also appends a year, (that has previously need extracted from a column in the question.csv file that is saved to another list and accessed via the index to match the answer to question five to the year the user was born in - if they've answered all the questiond correctly) to an empty list.

9. get_month() and get_day() - functions work very similarly to the answer_action() functions; however, they utilise *pyip.inputInt* from the *pyinputplus* package handle user input to get a integer between a specified range and continuously prompt the user for input until something suitable is entered. However, this can cause a ValueError as *pyip.inputInt* only takes integers. If a non-numeric value is entered, the ValueError is caught by an except statement and the user is again asked to input a number between a specified range.

10. results() - function to collate the users results with the user_answer_list variable to provide their results. This function takes the get_month() and get_day() functions as arguments. This input is then cast from a string to an integer and entered into the datetime.date() module inmportetd from the *datetime* package along with the year of the user's birth obtained from the answer to question five of the game. This outputs a datetime object that is then subtracted from the currect date (obtained by utilising the .today() method from the *datetime* package) to give the user's age in days. From there this answer is then converted to years through use of the *relativedelta* method in the imported *dateutil.relativedelta* package. The user is then told their age, a random fact is printed by using the *get_fact()* method from the imported package *randfacts*, and a custom fun fact is printed for the year of the user's birth by extracting the value pair via the key from a dictionary stored in the facts_dictionary.txt file.

11. available_results() - this function uses the built-in package *os*. The os.path.dirname method to get the absolute path to the cwd and save it in a local variable. os.path.join is then used to combine the abolute_path variable with a variable containing the reletive path to the desired directory and save this file path to another local variable, and finally this variable is used with os.listdir to print out a list of all the files inside the desired directory. This allows the user to view their options when choosing while file they wish to view.  

12. view_results(results) - takes available_results() function as an argument and uses a while loop with the condition True to continuously prompt the user to input the name of the file they wish to view. If the user inputs the name of a file that is in the desired directory, the file will be printed. If the user's input is invalid they are prompted to try again. KeyboardInterupt error can be caught by an excetion if the user inputs the string "quit"  to return the user to the main menu (it should not fully exit the program as SystemExit is not raised here, but rather break from the currently loop back to the main menu). A FileNotFoundError may occur if the user continually inputs a file name that does not exit in the desired dirrectory. The error is caught by an exception and the user is prompted again to input a correct file name.

13. save_results() - this function saves the results of the previous game to a new text file. The user's name is extracted from the global variable user_answer_list is used as the filename. The file is written to the desired directory using the same process as outlined about for accessing the directory, but is written using the 'x' value, meaning the filename must be unique and will not override another file if one exits with the same name. If the filename is already in use, the user is asked to input a custom filename. A try/except statement is utilised to catch any FileExistsError errors that may be thrown if the user repeatedly tries to save a file with a name that is already in use. The user is prompted again to enter a unique filename if this error is thrown. An UnboundLocalError error is thrown every time this function successfully executes; however, the function does what it is intended to do so a funny message is printed and the program returns to the main menu. 


## R7 - Develop an implementation plan.

To structure the implementation of the each step in creating the Terminal App, I have used a Trello board in the kanban project managment style to help me visualise the steps I need to complete and manage my time in doing so.

My Trello board is available here:
https://trello.com/b/A4RvTsvf/connie-jacques-terminal-app

Each card contains a neccissary action, details of the actions to be completed, and a timeframe. The timeframe for completing each step is represented with a coloured label. The key for the labels is as follows:

- Green: can be completed in under 30 minutes
- Yellow: can be completed in under 2 hours
- Orange: can be completed in 4 - 6 hours.

I hvae broken the steps down into enough detail that no card should take longer than 6 hours to complete. All cards held equal weight in terms of their priority and were placed from the top of the categorgy down in the anticipated order of completition, so that tasks that needed to be done before another could be started (such as cards containing steps to impliment functions that would be used by other functions) were done first by working from the top of the category to the bottom.

The stages of work are represented by four categories: Planned Tasks, In Progress, Completed Tasks and Nice to Have. All tasks were initalised in the Planned Tasks category and moved to In Progress and finally Completed Tasks as they undertaken and finalised.

The Nice to Have category contains a single card with a broad description to simply code a longer version of my Quiz Game, if time allows. Detail was not added to this card as it was unlikely there would be enough time to work on this card before the submission due date. In the end, there was not enough time to start work on this card and a second card was moved from the Planned Tasks categrogy to the Nice to Have category - "Code play again menu". Due to time contraints to complete the project, this task was abandond and one of it's steps (a user option to save the results of the previous game to a text file) was added to another card.

This planning method was highly successful in allowing me visualise the remaining workload, allocate appropriate time for each task and complete the project without forgetting to do any particular task.

The following screens were taken as I worked my through the project. Some show what is contain on an individual card, while others show overall progress. All of the cards can be accessed on Trello via the link provided above.

![Trelloboard at the start of the project](./docs/trello-start-project1.png)
![Trelloboard at the start of the project](./docs/trello-start-project2.png)
![Trelloboard at the start of the project](./docs/trello-start-project3.png)
![Trelloboard at the start of the project](./docs/trello-start-project4.png)
![Trelloboard card - use approval for app idea](./docs/trello-approval.png)
![Trelloboard card for Play Again menu - card is not particularly detailed as this idea was abandoned early on in the project due to time restraints, not enough time to complete](./docs/trello-play-again.png)
![Trelloboard card to create a function to access user's previous results](./docs/trello-previous-results.png)
![Trelloboard card - code a function to ask question three and handle the user input accordling](./docs/trello-question-three.png)
![Trelloboard card - create a function to display the game results to the user](./docs/trello-results.png)
![Update of Trelloboard showing progress](./docs/trello-update-questions1.png)
![Update of Trelloboard showing progress](./docs/trello-update-questions2.png)
![Update of Trelloboard showing progress](./docs/trello-update-results.png)
![Update of Trelloboard showing progress](./docs/trello-update.png)
![Update of Trelloboard showing progress](./docs/trello-update2.png)
![Update of Trelloboard showing progress](./docs/trello-update4.png)
![Trelloboard card - make executable card](./docs/trello-executable.png)
![Trelloboard at the end of the project](./docs/trello-end-project.png)


## R8 - Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

## HELP DOCUMENTATION

### How to install the Terminal App

Source code for the *Quiz Game* terminal application is available here: 

https://github.com/ConnieJacques/ConnieJacques_T1A3

To use the application, click on the green CODE button in the GitHub link, click over to the HTTPS tab and copy the url. Then, head over to your Terminal or Command Line and navigate into an appropriate directory to save the application in. Execute:

`
git clone https://github.com/ConnieJacques/ConnieJacques_T1A3.git
`

to clone the repository. Navigate into the /src directory.


Then, execute:

`
./setupgame.sh
`

This will check if you have python3 installed. If you do not already have python3 installed please check out this great installation guide:
https://wsvincent.com/install-python/

If you do have python3 installed, a virtual enviroment will be created and activated, and the program requirements will be installed before *Quiz Game* will automatically begin.

Once you are done playing the game execeute the command:

`
deactivate
`

in your terminal to close the virtual environment.

To use the *Quiz Game* command line application once it is running, simply follow the prompts in your terminal. Press ENTER once you have typed your answers to the questions you will be asked to move on to the next question.


### How to play the *Quiz Game*
Once installed, the game will launch immediately. If you have previously installed the game, you will need to navigate into the ConnieJacques_T1A3-main directory, change into the /src folder before executing:

`
./setupgame.sh
` 

to open the virtual envrionment and start a new game.

You will be asked a series of questions. The answers you provide to these questions will deternime the next question you are asked. Answer the questions correctly, and the *Quiz Game* will guess how old you are and give you a fun fact about the year you were born in and a bonus random fact to enjoy. If you fail to answer the questions correctly with regards to your own year of birth, the *Quiz Game* will not be able to guess your age correctly. You may need to consult Google for the correct answer, if you are unsure.You must be aged between 1 - 100 years or the game will not be able to guess your age. You can save your results to view later; however, if you choose not to save your rresults at the end of the each game, the results will be lost forever. Results will save to a folder called *previous game results* and can be accessed from the main game menu.

##### Disclaimer: Facts are not guaranteed to be true or accurate. This game is for the purpose of fun only.


### Dependancies required to install the Terminal App
The dependancies required for the *Quiz Game* Terminal App are: 

- attrs==22.1.0
- iniconfig==1.1.1
- packaging==22.0
- pluggy==1.0.0
- PyInputPlus==0.2.12
- PySimpleValidate==0.2.12
- pytest==7.2.0
- python-dateutil==2.8.2
- randfacts==0.19.0
- six==1.16.0
- stdiomask==0.0.6

Pip3 package management is used to download all of the dependancies and their requirements for the user from the requirements.txt file when the program is executed with the single command ./setupgamesh. A virtual environment is created and packages are installed within the venv. This will prevent most dependancy conflicts from arising.

### System and Hardware Requirements

Python3 is required to use this command line application. Python3 requires the following to work as expected:

- Linux/Ubuntu 16.04 to 17.10 (Debian or Fedora OS). Minimum 2GB RAM (4GB preferably). A minimum of 5GB available disk space is required as well as sudo access to the system.
- Windows 7 and up. Minimum 2GB RAM (4GB preferably). Minimum of 5GB available disk space
- MacOS - no minimum OS requirements. Minimum 2GB RAM (4GB preferably). Minimum of 5GB available disk space. Apple M1 Mac devices required Rosetta (a package than enables Intel-based features to run on Apple Silicon Macs) to be installed. To install Rosetta at the command line execute:

`
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
`

### how to use any command line arguments made for the application
The *Quiz Game* Terminal App requires the use of exactly one command line application:

`
./bash/sh
`
After cloning the repository, the user needs to navigate into the /src directory and execute the single command above. As long as they have python3 installed the application will run without the use of further command line commands. Use input is needed to navigate the application but simply requires the user to type their text into the command line and press ENTER.


## Link to Presentation Recording

The presentation can be accessed here:

https://vimeo.com/782201674


## R3 - References

**The following sources were utilised to write the questions for *Quiz Game*.**

Britroyals, n.d, *Kings & Queens - by Length of Reign*, Britroyals ,viewed on 6 December, 2022. Accessed at: https://britroyals.com/reigned.asp

Caregivers of America 2022, *2022 Generation Names Explained*, Caregivers of America, viewed on 6 December, 2022. Accessed at: https://caregiversofamerica.com/2022-generation-names-explained/

Goodreads, Inc. 2022, *By Decade Book Lists*, Goodreads, viewed on 6 December, 2022. Accessed at: https://www.goodreads.com/list/tag/by-decade

Hylands, Jesse and Stevens, Kylie 2022, *Clever Way Five Lions Escaped their Enclosure at Sydney's Taronga Zoo is Revealed - as Investigators Probe How Close they Came to Nearby Campers*, Daily Mail Australia, viewed on 6 December, 2022. Accessed at: https://www.dailymail.co.uk/news/article-11411245/Taronga-Zoo-lion-escape-Sydney-zoo-reveals-way-five-lions-managed-enclosure.html

Johal, Rumneek and Devlin, Megan, 2019, *67 things that happened this decade you probably forgot about*, DH News, viewed on 6 December, 2022. Accessed at: https://dailyhive.com/vancouver/things-that-happened-in-2010s

Statista, n.d, *International Box Office Figures for the Highest Grossing Movies Each Year, from 1915 to 2021*, Statista, viewed on 6 December, 2022. Accessed at: https://www.statista.com/statistics/1072778/highest-grossing-movie-annually-historical/
https://www.boxofficemojo.com/year/world/ 

Sonemic, Inc 2020, *Defining Bands/Artists of Each Decade*, Rate Your Mucis, viewed on 6 December, 2022. Accessed at: https://rateyourmusic.com/discussion/music/defining-bands_artists-of-each-decade/1/

The People History, 2022, *1800's to 2013*, The People History, viewed on 6 December, 2022. Accessed at: https://www.thepeoplehistory.com/


Vie, La 2020, *10 Interesting Facts That Happened So Far In 2020*, mobilestyles,
viewed on 6 December, 2022. Accessed at: https://mobilestyles.com/blog/posts/show/681-10-interesting-facts-that-happened-so-far-in-2020
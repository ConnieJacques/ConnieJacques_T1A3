import os


# Check if there are results saved in the directionary previous_game_results
def available_results():
    # Get absolute path to working directory
    absolute_path = os.path.dirname(__file__)
    # Provide relative path to the desired directory
    relative_path = "/previous_game_results"
    # Concatinate file paths together to give full path to previous_game_results
    full_path = os.path.join(absolute_path + relative_path)
    # Display a list of all the files currently in previous_game_results
    directory = os.listdir(full_path)
    print("These files are available:")
    for file in directory:
        print(file)

def view_results(results):
    try:
        # Get absolute path to working directory
        absolute_path = os.path.dirname(__file__)
        # Provide relative path to the desired directory
        relative_path = "/previous_game_results"
        # Concatinate file paths together to give full path to previous_game_results
        full_path = os.path.join(absolute_path + relative_path)
        directory = os.listdir(full_path)
        # Print a list of the avaiable results files
        results
        while True:
            # Prompt user to input name of the file they wish to open
            which_file = input("What file would you like to open? Do not include the file-extention. To exist enter QUIT\n")
            name_path = os.path.join(full_path + '/' + which_file)
            # Open the file if it exists
            if which_file in directory:
                with open(name_path) as f:
                    for line in f:
                        print(line.strip())
                return None
            # Exit if user wants to
            if which_file == 'quit':
                raise KeyboardInterrupt
            # If file name exists, display is of file in directory and prompt user to enter another name
            else:
                print("Whoops, that filename does not match any results.")
                results
                which_file = input("Please try again:\n")
                name_path = os.path.join(full_path + '/' + which_file)
                with open(name_path) as f:
                    for line in f:
                        print(line.strip())
                return None
    except KeyboardInterrupt:
        print("No worries!")
    except FileNotFoundError:
        # Give the user another chance by prompting again
        print("Whoops,no file with that name exists.")
        which_file = input("Please try again:\n")
        while True:
            name_path = os.path.join(full_path + '/' + which_file)
            if which_file in directory:
                with open(name_path) as f:
                    for line in f:
                        print(line.strip())
            # And another chance by prompting again
            else:
                print("Whoops, that filename does not match any results.")
                input("Please try again:\n")
                name_path = os.path.join(full_path + '/' + which_file)
                with open(name_path) as f:
                    for line in f:
                        print(line.strip())





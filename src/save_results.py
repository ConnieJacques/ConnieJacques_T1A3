import user_results
import os
import clear


# Save results from last game during the session  
def save_results():
    try:
        # Pull the user's name from the user_answer_list global variable to use as the filename, if not already in use
        filename = user_results.user_answer_list[1]
        # Get absolute path to working directory
        absolute_path = os.path.dirname(__file__)
        # Provide relative path to the desired directory
        relative_path = "/previous_game_results"
        # Concatinate file paths together to give full path to previous_game_results
        full_path = os.path.join(absolute_path + relative_path)
        # Concatinate full_file paths with the users name to create name and location for saving the file
        path_user_file = os.path.join(full_path + filename)
        # If user's name is not already a filename, create the file
        if os.path.exists(path_user_file) == False:
            with open(os.path.join(full_path, filename), 'x') as f:
                for line in user_results.user_answer_list:
                    f.write("%s\n" % line)
        # If the user's name is already in use, allow user to choose a name for the file and create it
        else:
            absolute_path = os.path.dirname(__file__)
            relative_path = "/previous_game_results"
            full_path = os.path.join(absolute_path + relative_path)
            custom_name = input("What would you like to call your file?\n")
        with open(os.path.join(full_path, custom_name), 'x') as f:
            for line in user_results.user_answer_list:
                f.write(line)
            return None
    # Catch error if file name already exists
    except FileExistsError:
        print('Whoops, a file with this name already exists')
        custom_name = input("What would you like to call your file?\n")
        with open(os.path.join(full_path, custom_name), 'x') as f:
            for line in user_results.user_answer_list:
                f.write(line)
    # Catch error thrown every time function is executed - doesn't stop the function for working as expected, so ignore error
    except UnboundLocalError:
        print("Nothing to see here!")
import user_results
import os


# filename = user_results.user_answer_list[1]


def save_results():
    try:
        filename = user_results.user_answer_list[1]
        absolute_path = os.path.dirname(__file__)
        relative_path = "/previous_game_results"
        full_path = os.path.join(absolute_path + relative_path)
        with open(os.path.join(full_path, filename), 'x') as f:
            f.write('user_results.user_answer_results')
    except FileExistsError:
        print('Whoops, a file with this name already exists')
        custom_name = input("What would you like to call your file?\n")
        with open(os.path.join(full_path, custom_name), 'x') as f:
            f.write('user_results.user_answer_results')
    
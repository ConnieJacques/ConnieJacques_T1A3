import user_results


# filename = user_results.user_answer_list[1]


try:
    filename = r'Connie.txt'
    with open(filename, 'x') as f:
        f.write('user_results.user_answer_results')
except FileExistsError:
    print('Whoops, a file with this name already exists')
    i = 10
    while i < 10:
        filename = r'Connie.txt' + str(i)
        with open(filename, 'x') as f:
            f.write('user_results.user_answer_results')
        i += 1
    
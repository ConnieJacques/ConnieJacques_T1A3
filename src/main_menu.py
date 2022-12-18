import os

# Clear terminal
def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# # Get and validate user's name
# def get_user_name():
#     print("To begin, please enter your name:")
#     while True:
#         user_name = input()
#         if not user_name.isalpha():
#             print("Please enter your name:")
#             continue
#         else:
#             return user_name

# def get_user_input():
#     user_input = input()
#     if user_input == "quit":
#         raise KeyboardInterrupt
    
#     return user_input

# def main_menu():
#     try:
#         print(f"Hi {get_user_name()}! What would you like to do?\n1. Play a new game\n2. View the results of a previous game\n3. Quit")
#         while True:
#             user_input = input()
#             if user_input.isnumeric():
#                 if user_input == "1":
#                     print("one")
#                 elif input == "2":
#                     print("two")
#                 elif input == "3":
#                     raise KeyboardInterrupt
#                 else:
#                     print("Please select 1, 2 or 3")
#                     pass
#     except KeyboardInterrupt:
#         clear_terminal()
#         print("It was fun while it lasted. See you next time!")

# print(user_input())
# print(main_menu())

# print(get_user_name())
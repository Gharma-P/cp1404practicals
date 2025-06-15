"""
Basic List Operations
"""

# numbers = []
# while len(numbers) < 5:
#     number = int(input("Enter a number: "))
#     numbers.append(number)
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[-1]))
# print("The smallest number is {}".format(min(numbers)))
# print("The largest number is {}".format(max(numbers)))
# print("The average number is {}".format(sum(numbers) / len(numbers)))

"""Woefully Inadequate Security Checker"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

get_user = input("Please enter username >>> ")
if get_user in usernames:
    print("You entered {}... Welcome".format(get_user))
else:
    print("Access Denied")


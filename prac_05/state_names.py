"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

#Loop that prints all the states and names
# for name, code in CODE_TO_NAME.items():
#     print(f"{name:3} is {code}")

state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()

#EAFP Approach
while state_code != "":
    try:
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid state")
    state_code = input("Enter short state: ").upper()



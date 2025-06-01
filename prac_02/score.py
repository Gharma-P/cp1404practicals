"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Error")
elif score <= 49:
    print("Bad")
elif score < 90:
    print("Pass")
elif score <= 100:
    print("Excellent")
else:
    print("Error")



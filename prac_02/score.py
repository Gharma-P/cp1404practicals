"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def get_score_result(score):
    if score < 0 or score > 100:
        return "Error"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    print(get_score_result(score))
    random_score = random.randint(0, 100)
    print(f"Random Score: {random_score}, Result: {get_score_result(random_score)}")

main()





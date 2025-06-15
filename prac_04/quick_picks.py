"""
Write a program asking users how many quick picks they wish to generate
"""
import random
MAX = 45
MIN = 1
NUMBER = 6

def sort_pick():
    picks = []
    while len(picks) < NUMBER:
        random_number = random.randint(MIN, MAX)
        if random_number not in picks:
            picks.append(random_number)
    picks.sort()
    return picks

def main():
    get_picks = int(input("How many picks would you like to generate? "))
    for n in range(get_picks):
        picks = sort_pick()
        line = " ".join(f"{n:2}" for n in picks)
        print(line)

main()

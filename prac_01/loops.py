"""
Program to display numbers differently
"""

#a Count in 10's from 0 - 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

#b Count down from 20 - 1
for x in range(20, 0, -1):
    print(x, end=' ')
print()


#c print n stars (*)
stars = int(input("Number of starts: "))
for stars in range(0, stars, 1):
    print("*", end=' ')
print()


#d Print n lines of increasing stars
for stars in range(0, stars, 1):
    print("*" * stars)
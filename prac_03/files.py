# 1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

# 3.
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    print(first_number + second_number)

# 4.
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line)
    print(total)

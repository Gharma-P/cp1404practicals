"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    record = []
    for line in input_file:
        # print(line) # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        record.append(parts)
        # print(parts)  # See if that worked
        # print("----------")
    input_file.close()
    return record


def display_data(record):
    for parts in record:
        print("{} is taught by {:12} and has {:3} students".format(parts[0], parts[1], parts[2]))


main()

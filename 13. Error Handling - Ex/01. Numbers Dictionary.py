numbers_dictionary = {}  # one:1 ....

line = input()
while line != "Search":
    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number  # Запис на числото
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()
while line != "Remove":
    searched = line

    try:
        print(numbers_dictionary[searched])  # принтиране на числото на конзолата
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]   # Изтриване на числото от db
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)

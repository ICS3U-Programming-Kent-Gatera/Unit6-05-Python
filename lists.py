#!/usr/bin/env python3

# Created by: Kent G
# Date: Dec.15, 2022
# This program gets marks from the user
# and then prints the average of the marks


def average_mark(marks):

    # Returns the average of all marks in the list
    return sum(marks) / len(marks)


def main():
    # Creates an empty list for the user's marks
    user_marks = []

    print("Enter a mark of '-1' if you have finished entering marks")

    while True:

        # Tests if the mark entered is a number
        try:
            mark = float(input("Enter a mark: "))
        except:
            print("You must enter a numeric value")
            continue

        else:
            # If the mark is not equal to -1, then the user
            # is asked to enter another mark
            if mark != -1:
                user_marks.append(mark)
                continue

            # Prints the average of the marks entered
            print(f"The average of your marks is {average_mark(user_marks)}%.")
            break


if __name__ == "__main__":
    main()

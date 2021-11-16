# Program 1: PUP Grading System
# Create a pogram that will ask for grade percentage.
# Display the equivalent Grade/Mark and Description.
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good


def evaluate(grade):
    if grade >= 97 and grade <= 100:
        print('Grade/Mark: 1.00')
        print('Description: Excellent')
    elif grade >= 94 and grade <= 96:
        print('Grade/Mark: 1.25')
        print('Description: Excellent')
    elif grade >= 91 and grade <= 93:
        print('Grade/Mark: 1.5')
        print('Description: Very Good')
    elif grade >= 88 and grade <= 90:
        print('Grade/Mark: 1.75')
        print('Description: Very Good')
    elif grade >= 85 and grade <= 87:
        print('Grade/Mark: 2.0')
        print('Description: Good')
    elif grade >= 82 and grade <= 84:
        print('Grade/Mark: 2.25')
        print('Description: Good')
    elif grade >= 79 and grade <= 81:
        print('Grade/Mark: 2.5')
        print('Description: Satisfactory')
    elif grade >= 76 and grade <= 78:
        print('Grade/Mark: 2.75')
        print('Description: Satisfactory')
    elif grade == 75:
        print('Grade/Mark: 3.0')
        print('Description: Passing')
    elif grade >= 65 and grade <= 74:
        print('Grade/Mark: 5.0')
        print('Description: Failure')


import math

gradeInput = float(input('Insert grade: '))
gradeRounded = math.ceil(gradeInput)

evaluate(gradeInput)
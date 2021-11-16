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
    else:
        print('Invalid grade percentage. Please input grade percentage from 65 to 100 only.')
        
import math

print('Welcome to PUP Grading System!')
print('Kindly follow the instructions to evaluate your grade percentage.')

studentStatus = input('Before you proceed, are you either incomplete, withdrawn, or dropped? Type YES if you are. If not, type NO: ').upper()
if studentStatus == 'YES':
    status = input('Insert your current status: ').upper()
    if status == 'INCOMPLETE':
        print('Grade/Mark: Inc.')
        print('Description: Incomplete')
    elif status == 'WITHDRAWN':
        print('Grade/Mark: W')
        print('Description: WITHDRAWN')
    elif status == 'DROPPED':
        print('Grade/Mark: D')
        print('Description: Dropped')
    else:
        print('Invalid status. Please input either INCOMPLETE, WITHDRAWN, or DROPPED.')
elif studentStatus == 'NO':
    gradeInput = float(input('Insert your grade percentage: '))
    gradeRounded = math.ceil(gradeInput)
    evaluate(gradeRounded)
else:
    print('Invalid input. Please input either YES or NO.')
# Program 3: Life Stages
# Create a program that ask for an age of a person
# Display the life stage of the person
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

# # Steps 

# OUTPROACH NUMBER 1
# 1. ask age, convert, store
print('Welcome to Know-Your-Life-Stage-Inator!')
age = int(input('Kindly enter your current age: '))
# 2. test 0 - 12
if age <= -1:
    print('INVALID AGE. TRY AGAIN.')
else:
    if age > -1 and age <= 12:
        print('Your current life stage is: Kid')
# 3. test 13 - 17
    else: 
        if age >= 13 and age <= 17:
            print('Your current life stage is: Teen')
# 4. test 18
        else:
            if age == 18:
                print('Your current life stage is: Debut')
# 5. test >= 19
            else:
                if age >= 19:
                    print('Your current life stage is: Adult')

# 6. print closing statement
print('Identification Complete.')
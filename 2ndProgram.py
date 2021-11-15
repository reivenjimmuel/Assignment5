# Program 2: Find the lowest number
# Create a program that ask 3 numbers.
# Find the lowest numer using only if-else statement.
# Display the lowest number

def evaluateLowest(firstN_, secondN_, thirdN_):
    if firstN_ < secondN_ and firstN_ < thirdN_:
        print(f'{firstN_} is the lowest number among the three.')
    else:
        if secondN_ < firstN_ and secondN_ < thirdN_:
            print(f'{secondN_} is the lowest number among the three.')
        else:
            if thirdN_ < firstN_ and thirdN_ < secondN_ :
                print(f'{secondN_} is the lowest number among the three.')

print('Which is the Lowest Number?')

firstNumber = int(input('Insert the first number of your choice: '))
secondNumber = int(input('Insert the second number of your choice: '))
thirdNumber = int(input('Insert the third number of your choice: '))

evaluateLowest(firstNumber, secondNumber, thirdNumber)
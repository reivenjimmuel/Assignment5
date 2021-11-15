# Program 2: Find the lowest number
# Create a program that ask 3 numbers.
# Find the lowest numer using only if-else statement.
# Display the lowest number

def evaluateLowest(fN, sN, tN):
    if fN < sN and fN < tN:
        print(f'{fN} is the lowest number among the three.')
    elif sN < fN and sN < tN:
        print(f'{sN} is the lowest number among the three.')
    elif tN < fN and tN < sN :
        print(f'{tN} is the lowest number among the three.')
    elif fN == sN and fN < tN:
        print(f'{fN} is the lowest number among the three.')
    elif fN == tN and fN < sN:
        print(f'{fN} is the lowest number among the three.')
    elif sN == tN and sN < fN:
        print(f'{sN} is the lowest number among the three.')
    else:
        print(f'{fN} is the lowest number among the three.')

print('Which is the Lowest Number?')
print('Note: Decimals are not accepted.')

firstNumber = int(input('Insert the first number of your choice: '))
secondNumber = int(input('Insert the second number of your choice: '))
thirdNumber = int(input('Insert the third number of your choice: '))

evaluateLowest(firstNumber, secondNumber, thirdNumber)
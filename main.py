'''
    Calculator - Functions
Addition:
Subtraction:
Division:
Multiplication:
Remainder:
Power of (exponents):
'''

##Functions to perform calculator operations
def add(x, y):
    ans = x + y
    return ans


def subtract(x, y):
    ans = x - y
    return ans


def divide(x, y):
    ans = x / y
    return format(ans, '.2f')


def multiply(x, y):
    ans = x * y
    return ans


def remainder(x, y):
    ans = x % y
    return ans


def power_of(x, y):
    ans = x ** y
    return ans


##Calculator Operations
def calculator(choice):
    while (choice != 'E'):
        if choice == 'A':
            num1 = int(input('Enter your first number: '))
            num2 = int(input('Enter your second number: '))

            print(f'\t{num1} + {num2} = ', add(num1, num2))

        elif choice == 'S':
            num1 = int(input('Enter your first number: '))
            num2 = int(input('Enter your second number: '))

            print(f'\t{num1} - {num2} = ', subtract(num1, num2))

        elif choice == 'D':
            num1 = int(input('Enter your first number: '))
            num2 = int(input('Enter your second number: '))

            print(f'\t{num1} / {num2} = ', divide(num1, num2))

        elif choice == 'M':
            num1 = int(input('Enter your first number: '))
            num2 = int(input('Enter your second number: '))

            print(f'\t{num1} x {num2} = ', multiply(num1, num2))

        elif choice == 'R':
            num1 = int(input('Enter your first number: '))
            num2 = int(input('Enter your second number: '))

            print(f'\t The remainder of {num1} / {num2} is: ', remainder(num1, num2))

        elif choice == 'P':
            num1 = int(input('Enter your base number: '))
            num2 = int(input('Enter your exponents number: '))

            print(f'\t {num1} to the power of {num2} is: ', power_of(num1, num2))

        else:
            print('\tIncorrect input entered: \n')

        user_input = input('Enter a letter to choose: \n')
        choice = user_input.upper()


##How to operate
def calcu():
    print('***Calculator***')
    print("""
    Enter 'A' to add two numbers: 
    Enter 'S' to subtract two numbers:
    Enter 'D' to divide two numbers:
    Enter 'M' to multiply two numbers:
    Enter 'R' to get the remainder: 
    Enter 'P' to get an exponential expression:
    Enter 'E' to exit program:
    """)

    user_input = input('Enter a letter to choose: \n')
    choice = user_input.upper()

    calculator(choice)


calcu()




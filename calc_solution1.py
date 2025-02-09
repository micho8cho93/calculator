"""Your task is to create a calculator program that runs in the CLI.
Follow the instructions below and run the test file whenever you're ready 
to check if your program is correct."""

#Create a function to return two added numbers
def add(num1, num2):
    return num1 + num2

#Create a function to return two subtracted numbers
def subtract(num1, num2):
    return num1 - num2

#Create a function to return two multiplied numbers
def multiply(num1, num2):
    return num1 * num2

#Create a function to return two divided numbers
def divide(num1, num2):
    return num1 / num2

#Create a function to return the remainder of two numbers
def remainder(num1, num2):
    return num1 % num2

#Create a function to return the exponent of two numbers
def exponent(num1, num2):
    return num1 ** num2

#Create menu of options to let user decide which function they want to use
#Print menu of options
#Get user input
#Run program that user selected
def program():
    print('Select the program you wish to run: ')
    print('1: Addition')
    print('2: Subtraction')
    print('3: Multiplication')
    print('4: Division')
    print('5: Remainder')
    print('6: Exponent')

#Run the function that the user requests
    choice = input('Enter program number here: ')
    
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))

    if choice == '1':
        print(add(num1, num2))
    elif choice == '2':
        print(subtract(num1, num2))
    elif choice == '3':
        print(multiply(num1, num2))
    elif choice == '4':
        print(divide(num1, num2))
    elif choice == '5':
        print(remainder(num1, num2))
    elif choice == '6':
        print(exponent(num1, num2))

if __name__ == "__main__":
    program()

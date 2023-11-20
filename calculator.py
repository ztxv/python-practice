import math
import os
#11/19/23


class Main:
    
    def operations():
        print(" ")
        print("Addition, Subtraction, Multiplication, Division, Squared, Square Root (sqrt)\n")
        operation = input("Enter which operation you would like to do: ")
        return operation.lower()
        




def addition_operation():
    print('You have picked addition! \n')
    x = int(input('What is the first number: '))
    y = int(input('What is the second number: '))
    quotient = (int(x) + int(y))
    print("The sum is", quotient)
    restart = input('Would you like to try again? (y or )')
    if restart == "y":
        main()
    elif restart == "n":
        exit()
    
def division_operation():
    print('You have picked division! \n')
    x = int(input('What is the dividend: '))
    y = int(input('What is the divisor: '))
    sum = (int(x) / int(y))
    print("The quotient is", sum)
    restart = input('Would you like to try again? (y or n)')
    if restart == "y":
        main()
    elif restart == "n":
        exit()
    
    
def multiplication_operation():
    print('You have picked multiplication! \n')
    x = int(input('What is the first factor: '))
    y = int(input('What is the second factor: '))
    product = (int(x) * int(y))
    print("The product is", product)
    restart = input('Would you like to try again? (y or n)')
    if restart == "y":
        main()
    elif restart == "n":
        exit()
    
    
def subtraction_operation():
    print('You have picked subtraction! \n') 
    x = int(input('What is the minuend: '))
    y = int(input('What is the subtrahend: '))
    difference = (int(x) - int(y))
    print("The difference is", difference ) 
    restart = input('Would you like to try again? (y or n)')
    if restart == "y":
        main()
    elif restart == "n":
        exit()   
    
def squared_operation():
    print('You have picked squaring! \n')
    x = int(input("Please enter the base: "))
    squared = (int(x) * int(x))    
    print("The answer is", squared)
    print("/n")
    restart = input('Would you like to try again? (y or n)')
    if restart == "y":
        main()
    elif restart == "n":
        exit()
    
    
def square_root():
    x = int(input("What is the radicand: "))
    sqrt = (int(x))
        

def main():
    operation = Main.operations()


    if operation == "addition":
        addition_operation()
    elif operation == "subtraction":
        subtraction_operation()
    elif operation ==  "multiplication":
        multiplication_operation()
    elif operation == "division":
        division_operation()
    elif operation == "squared":
        squared_operation()
    elif operation == "sqrt":
        square_root()
    





main()

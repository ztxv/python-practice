
#11/19/23


def calculation():
    print("\n")
    print("Addition (+), Subtraction (-), Division (/), Multiplication (*)")
    print("\n")
    calculation = input("Type in what you would like to calculate: ")
    
    try:
        result = eval(calculation)  # Using eval to evaluate the user input
        print(f"Your answer is: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
           
        
calculation()
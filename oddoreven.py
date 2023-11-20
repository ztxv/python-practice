#11/19/23

def oddoreven():
    print("Check if a number is odd or even :D \n")
    userinput = int(input("Type the number you would like to evaluate: "))
    
    if userinput % 2 == 0:
        print(f"{userinput} is even")
    else:
        print(f"{userinput} is odd")
    
    
oddoreven()
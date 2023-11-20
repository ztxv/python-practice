#11/19/23


#asks the user which conversion it would like to do, checks the input, and calls the according function for that conversion


def asktemp():
    answer = input("\nWould you like to convert to Celsius or to Fahrenheit (C or F): ")
    if answer.lower() == "c":
        tocelsius()
    elif answer.lower() == "f":
        tofahrenheit()
    else:
        print("\nError, please type either C or F")
        asktemp()
   
# this is to check the temperature input to see if its an integer or not
def check_int(prompt):
       while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("\nError: Please try entering a whole number.")
   
 #converts celsius to fahrenheit
        
def tofahrenheit():
    temp = check_int("\nType the temperature you would like to convert to Fahrenheit: ")
    output = ((9/5) * temp) + 32
    print(f"{temp}, is {output}, in Fahrenheit")
    tryagain()
    
    #converts fahrenheit to celsius
    
def tocelsius():
    temp = check_int("\nType the temperature you would like to convert to Celsius: ")
    output = 5/9 * (temp - 32)
    print(f"{temp}, is {output}, in Celsius")
    tryagain()
    
    #allow user to convert temps as much a they will
    
def tryagain():
    yesorno = input("Would you like to do another conversion? (Y or N): ")
    if yesorno.lower() == "y":
        asktemp()
    elif yesorno.lower() == "n":
        exit()
    else:
        print("Please type either Y or N")
        tryagain()
    
asktemp()
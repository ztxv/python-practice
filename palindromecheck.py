#11/20/23


def reversedstring():
    print("\nA 'Palindrome' is a word that is the same forwards and backwords \n")
    thestring = str(input("Type the string you would like to check to see if its a Palindrome: "))
    reversed = thestring.lower()[::-1]
    if reversed == thestring.lower():
        print( thestring + " is a Palindrome!")
        tryagain()
    else:
        print( thestring + " is not a Palindrome")
        tryagain()
    

def tryagain():
    yesorno = input("Would you like to do another? (Y or N): ")
    if yesorno.lower() == "y":
        reversedstring()
    elif yesorno.lower() == "n":
        exit()
    else:
        print("Please type either Y or N")
        tryagain()   
    
    
reversedstring()

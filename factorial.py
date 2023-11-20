#11/1/23
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def tryagain():
    again = input("Again? (Y) or (N): ")
    if again.lower() == "y":
        factorial()
    elif again.lower() == "n":
        exit()
    else:
        print("Please type either Y or N")
        tryagain()

# Example usage

def factorial():
    number = int(input("Type the number you would like to factor: "))
    result = factorial_iterative(number)
    print(f"The factorial of {number} is {result}")
    print("\n")
    tryagain()
        


factorial()
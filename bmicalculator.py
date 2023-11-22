#11/22/23



#Determine which units to calculate the BMI

def whichcalc():
    calc = input("Would you like to use the Freedom Units or Metric Units: ")
    if calc.lower() == "freedom":
        imperialcalculator()
    elif calc.lower() == "metric":
        metriccalculator()
    else:
        print("\nChoose either Metric or Freedom Units")
        whichcalc()


#bmi calculator but for americans

def imperialcalculator():
    weight = float(input("How much do you weight in pounds(lbs): "))
    height = float(input("How tall are you inches (in): "))
    #formula for BMI in imperial units
    rawbmi = (weight / (height ** 2)) * 703
    #rounds the original bmi to the tenths to get accurate BMI 
    bmi = round(rawbmi, 1)
    #checks the bmi to see where it ranks
    if bmi < 18.5:
        bmirank = str("Underweight")
    elif 18.5 <= bmi < 25:
        bmirank = str("Normal weight")
    elif 25 <= bmi < 30:
        bmirank = str("Overweight")
    else:
        bmirank = str("Obese")
        #tells user his BMI and what it means
    print("Your BMI is", bmi)
    print("You are", bmirank)
    


#bmi calculator for everyone else in the world

def metriccalculator():
    weight = float(input("How much do you weight in kilograms(kg): "))
    height = float(input("How tall are you meters (m): "))
    rawbmi = weight / (height ** 2)
    bmi = round(rawbmi, 1)
    if bmi < 18.5:
        bmirank = str("Underweight")
    elif 18.5 <= bmi < 25:
        bmirank = str("Normal weight")
    elif 25 <= bmi < 30:
        bmirank = str("Overweight")
    else:
        bmirank = str("Obese")
    print("Your BMI is", bmi)
    print("Your BMI is", bmi)
    
    
    

whichcalc()
#Weight Function
def getWeight(system):
    if system == "metric":
        weight = float(input("Enter your weight in Kilograms:"))
    else:
        weight = float(input("Enter your weight in Pounds"))
        weight = weight * 0.453592 #Converts Pounds to Kilograms
    return weight
#Height Function (Split Strings for Imperial System)
def getHeight(system):
    if system == "metric":
       height = float(input("Enter your height in Centimetres."))
       height = height/100 #Converts cm to metres.
    else:
        inputString = input("Enter your height in Feet & Inches (example: 5'8\")")
        splitString = inputString.split("'")
        feet = float(splitString[0])
        inches = float(splitString[1].strip('"'))
        total_inches = (feet * 12) + inches
        height = total_inches * 0.0254  # convert inches to meters
    return height

#BMI Function
def calculateBMI(weight, height):
    return weight / (height ** 2)

#BMI Category Function (Elseif ladder)
def getBMICategory(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
#Main Function
if __name__ == "__main__":
    print("Welcome to the BMI Calculator!")
    system= input("Which system are you opting to use? (metric/imperial)").strip().lower()

    if system not in ["metric", "imperial"]:
        print("Invalid System selected.Please enter from the above two unit systems.")
    else:
        weight = getWeight(system)
        height = getHeight(system)
        bmi = calculateBMI(weight, height)
        category = getBMICategory(bmi)

        print(f"\nYour Final BMI is:{round(bmi,2)}")
        print(f"According to your BMI, you are categorized as {category}")




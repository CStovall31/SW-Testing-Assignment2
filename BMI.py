from math import pow

#Inputs
weight = float(input("Enter weight in lbs: "))
height = float(input("Enter height in inches: "))

#Calculate Body Mass Index
def BMI_calc(weight, height):

    weight = float(weight) * 0.45

    height = float(pow(height * 0.025, 2))

    BMI = format((weight / height), ".1f")

    #Determine if underweight
    if float(BMI) < 18.5:
        category = "Underweight"

    #Determeine if normal weight
    elif float(BMI) > 18.5 and float(BMI) < 24.9:
        category = "Normal weight"

    #Determine if Overweight
    elif float(BMI) > 25 and float(BMI) < 29.9:
        category = "Overweight"

    #Deteremine if Obese
    elif float(BMI) > 30:
        category = "Obese"

    print(BMI, category)

    return BMI, category


BMI_calc(weight, height)





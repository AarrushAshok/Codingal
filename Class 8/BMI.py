#BMI
def BMI():
    weight = float(input("Enter your weight in kilograms:"))
    height = float(input("Enter your height in meters:"))

    if weight<= 0 or height <= 0:
        print("Weight and height must be positive numbers")

    bmi = weight/ (height*height)
    bmi = round(bmi,2)

    if bmi < 18.5:
        print("Your BMI is:",bmi)
        print("You are Underweight")
    elif bmi < 25:
        print("Your BMI is:",bmi)
        print("You are Normal Weight")
    elif bmi < 30:
        print("Your BMI is:",bmi)
        print("You are OverWeight")
    else:
        print("Your BMI is:",bmi)
        print("You are Obese")

BMI()
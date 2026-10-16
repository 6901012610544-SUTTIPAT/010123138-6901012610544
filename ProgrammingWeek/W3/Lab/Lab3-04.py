def calculate_BMI(weight, height):
    height = height / 100
    bmi = weight / height**2
    return bmi

def interpret_BMI(bmi):
    if bmi >= 40:
        return "Class 3 Obesity (Severe Obesity)"
    elif bmi >= 35 and bmi < 40:
        return "Class 2 Obesity"
    elif bmi >= 30 and bmi < 35:
        return "Class 1 Obesity"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Healthy Weight"
    else:
        return "Underweight"

if __name__ == '__main__':
    weight, height = map(int, input("Enter your weight in kilogram\nand your height in centimeter: ").split())
    print(f"Your BMI is: {calculate_BMI(weight, height):.2f} kg/m^2")
    print(f"That's mean you are: {interpret_BMI(calculate_BMI(weight, height))}")
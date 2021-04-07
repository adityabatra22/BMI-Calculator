#BMI Calculator

print("\n<<<<<<<<<<<<<-BMI Calculator->>>>>>>>>>>>>\n")

def bmi_calculator(weight, height):

    '''
        This function is used to calculate bmi of a person.

        Argunment : weight(float), height(float)
        Return : bmi(float)
    '''
    height = height/100
    return weight/(height*height)

weight = float(input("Enter your weight in kilograms : "))
height = float(input("Enter your height in centimeters : "))

bmi = bmi_calculator(weight, height)

print(f'Your BMI is {round(bmi,2)}')

if bmi < 0:
    print("Please Enter Vaid Details.....") 
elif bmi < 18.5:
    print("Underweight.")
elif 18.5 <= bmi <= 24.9:
    print("Normal Weight.")
elif 25.0 <= bmi <= 29.9:
    print("Overweight.")
else:
    print("Obesity.")
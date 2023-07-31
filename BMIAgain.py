'''BMIAgain'''
def bmiagain(weight, tall):
    '''BMIAgain'''
    bmi = weight/((tall/100)**2)
    if bmi < 18:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    else:
        print("Obese")
bmiagain(int(input()), int(input()))

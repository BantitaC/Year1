'''Body Mass Index'''
def bmi(name, weight, tall):
    '''Body Mass Index'''
    process1 = name + "\'s  BMI = %.2f" % (weight/((tall/100)**2))
    print(process1)
    return
def bmi1():
    '''input'''
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
bmi1()
bmi(input(), float(input()), float(input()))

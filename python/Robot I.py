'''Robot I'''
def robot(name, age):
    '''check name and age'''
    if age < 18:
        print(name, "you can pass.", sep=", ")
    else:
        print(name, "you shall not pass.", sep=", ")
robot(input(), float(input()))

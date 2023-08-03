'''Triangle I'''
def triangle(wood1, wood2, wood3):
    '''Triangle I'''
    fmn = findmn(wood1, wood2)
    result1 = findmn(fmn, wood3)
    fmx = findmx(wood1, wood2)
    result2 = findmx(fmx, wood3)
    if wood1 > result1 and wood1 < result2:
        mid = wood1
    elif wood2 > result1 and wood2 < result2:
        mid = wood2
    else:
        mid = wood3

    if (((mid ** 2) + (result1 ** 2))**0.5) <= ((result2**2)**0.5) + 0.01:
        print("Yes")
    else:
        print("No")

def findmx(num1, num2):
    '''find max'''
    if num1 > num2:
        return num1
    return num2

def findmn(num1, num2):
    '''find min'''
    if num1 < num2:
        return num1
    return num2
triangle(float(input()), float(input()), float(input()))

'''Largest Number'''
def largestnum(num1, num2, num3):
    '''Largest Number'''
    fmx = findmx(num1, num2)
    fmx2 = findmx(fmx, num3)
    fmn = findmn(num1, num2)
    fmn2 = findmn(fmn, num3)
    if num1 > fmn2 and num1 < fmx2:
        mid = num1
    elif num2 > fmn2 and num2 < fmx2:
        mid = num2
    else:
        mid = num3
    fmx2, mid, fmn2 = str(fmx2), str(mid), str(fmn2)
    print(int(fmx2+mid+fmn2))

def findmx(num1, num2):
    '''find max'''
    if num1 > num2:
        return num1
    return num2

def findmn(num1, num2):
    '''find max'''
    if num1 < num2:
        return num1
    return num2
largestnum(abs(int(input())), abs(int(input())), abs(int(input())))

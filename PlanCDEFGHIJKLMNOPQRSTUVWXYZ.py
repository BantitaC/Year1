'''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
def plan(choose, num1, num2, num3):
    '''find ascend or descend'''
    if choose == "Ascend":
        fmn = findmn(num1, num2)
        fmn1 = findmn(fmn, num3)
        fmx = findmx(num1, num2)
        fmx1 = findmx(fmx, num3)
        if num1 > fmn1 and num1 < fmx1:
            mid = num1
        elif num2 > fmn1 and num2 < fmx1:
            mid = num2
        else:
            mid = num3
        print("%.2f, %.2f, %.2f" % (fmn1, mid, fmx1))

    elif choose == "Descend":
        fmn = findmn(num1, num2)
        fmn1 = findmn(fmn, num3)
        fmx = findmx(num1, num2)
        fmx1 = findmx(fmx, num3)
        if num1 > fmn1 and num1 < fmx1:
            mid = num1
        elif num2 > fmn1 and num2 < fmx1:
            mid = num2
        else:
            mid = num3
        print("%.2f, %.2f, %.2f" % (fmx1, mid, fmn1))

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

plan(input(), float(input()), float(input()), float(input()))

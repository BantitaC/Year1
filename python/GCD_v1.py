'''GCD_v1'''
def hrm(num1, num2):
    '''GCD_v1'''
    dvs = min(num1, num2)
 
    if num1 == 0 or num2 == 0:
        dvs = max(num1, num2)
        print(dvs)
        dvs = 0
 
    while dvs > 0:
        if num1 % dvs == 0 and num2 % dvs == 0 and num1 <= 100000 and num2 <= 100000:
            print(dvs)
            break
        dvs -= 1
 
hrm(int(input()), int(input()))

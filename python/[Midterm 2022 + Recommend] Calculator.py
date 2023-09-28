'''[Midterm 2022 + Recommend] Calculator'''
def calculator(num):
    '''[Midterm 2022 + Recommend] Calculator'''
    keep = 0
    for i in range(1, num + 1):
        if num == 1:
            keep += 1
        elif len(str(i)) >= 1:
            keep += len(str(i)) + 1
    print(keep)
 
calculator(int(input()))

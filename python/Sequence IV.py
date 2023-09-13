'''Sequence IV'''
def sequence(num):
    '''Sequence IV'''
    num1 = 1
    for _ in range(1, num + 1):
        for _ in range(1, num + 1):
            print(num1, end=" ")
            num1 += 1
        print()
 
sequence(int(input()))

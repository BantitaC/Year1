'''Sequence V'''
def sequence(num):
    '''Sequence V'''
    for i in range(num):
        if i % 7 == 0 and i != 0:
            print()
        print(num, end=" ")
        num -= 1
 
sequence(int(input()))

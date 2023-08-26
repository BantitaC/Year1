'''Sequence I'''
def sequence(num):
    '''Sequence I'''
    for _ in range(1, num+1, 1):
        for i in range(1, num+1, 1):
            print(i, end=" ")
        print()
sequence(int(input()))

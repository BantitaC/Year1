'''Sequence N'''
def sequence(num):
    '''Sequence N'''
    for i in range(num):
        for j in range(num):
            if i == j or j == num - 1 or j == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
 
sequence(int(input()))

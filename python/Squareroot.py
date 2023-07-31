'''Squareroot'''
def root(num_x, num_y):
    '''check if it's Squareroot'''
    if num_x**2 == num_y:
        print(True)
    else:
        print(False)
root(int(input()), int(input()))

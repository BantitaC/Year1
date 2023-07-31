'''ODD_EVEN'''
def is_odd(num):
    '''Check if the received number is even or odd.'''
    if num % 2 != 0:
        print(True)
    else:
        print(False)
is_odd(int(input()))

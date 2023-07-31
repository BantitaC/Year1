'''Circular II'''
def circular(me_x, me_y, me_r, friend_x, friend_y):
    '''Circular II'''
    f_r = float(input())
    process = (((me_x - friend_x) ** 2) + ((me_y - friend_y) ** 2)) ** 0.5
    if process < me_r + f_r:
        print("Yes")
    else:
        print("No")
circular(float(input()), float(input()), float(input()), float(input()), float(input()))

'''Circular I'''
def circular(me_x, me_y, radius, mosquito_x, mosquito_y):
    '''Circular I'''
    process = (((me_x - mosquito_x) ** 2) + ((me_y - mosquito_y) ** 2)) ** 0.5
    if process <= radius:
        print("Yes")
    else:
        print("No")
circular(float(input()), float(input()), float(input()), float(input()), float(input()))

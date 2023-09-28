'''[Midterm 2020] Books'''
import math

def books(amount, pages, var_x, var_y):
    '''[Midterm 2020] Books'''
    page = 0
    day = 0
    count = 0
    while True:
        processpage = math.ceil((var_x / var_y) * pages)
        if amount == count:
            break
        if processpage >= pages:
            break
        page += processpage
        if page >= pages:
            count += 1
            page = 0
        var_x += 1
        var_y += 1
        day += 1
    day += amount - count
    print(day)

books(int(input()), int(input()), int(input()), int(input()))

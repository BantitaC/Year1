'''Point in Circle'''
def circle(var_x, var_y, var_r, var_xn, var_yn):
    '''Point in Circle'''
    process = ((((var_x-var_xn)**2) + ((var_y-var_yn)**2))**0.5)
    if process <= var_r:
        print(True)
    else:
        print(False)
circle(float(input()), float(input()), float(input()), float(input()), float(input()))

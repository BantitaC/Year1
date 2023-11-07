'''PH'''
def phh(val):
    '''PH'''
    if val >= 0 and val < 7:
        print("acidic")
    elif val == 7:
        print("neutral")
    elif val > 7 and val <= 14:
        print("akaline")
    else:
        print("error")

phh(float(input()))

'''Fever'''
def fever(temp):
    '''Fever'''
    if temp >= 36 and temp < 38:
        print("No Fever")
    elif temp >= 38 and temp < 39:
        print("Mild Fever")
    elif temp >= 39 and temp < 40:
        print("High Fever")
    elif temp >= 40 and temp <= 43:
        print("Very High Fever")

fever(float(input()))

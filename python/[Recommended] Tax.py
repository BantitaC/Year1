'''[Recommended] Tax'''
def tax(age, size, keep):
    '''[Recommended] Tax'''
    if age < 6:
        if 1 <= size <= 600:
            keep += size * 0.5
        elif 600 < size <= 1800:
            keep += 600 * 0.5
            keep += (size - 600) * 1.5
        elif size > 1800:
            keep += 600 * 0.5
            keep += (1800 - 600) * 1.5
            keep += (size - 1800) * 4
    else:
        if 1 <= size <= 600:
            keep += size * 0.5
        elif 600 < size <= 1800:
            keep += 600 * 0.5
            keep += (size - 600) * 1.5
        elif size > 1800:
            keep += 600 * 0.5
            keep += (1800 - 600) * 1.5
            keep += (size - 1800) * 4
        keep -= (discount(age) * keep)
    print("%.2f" % keep)

def discount(age):
    '''discount tax'''
    if age == 6:
        return 10/100
    elif age == 7:
        return 20/100
    elif age == 8:
        return 30/100
    elif age == 9:
        return 40/100
    elif age >= 10:
        return 50/100

tax(int(input()), int(input()), 0)

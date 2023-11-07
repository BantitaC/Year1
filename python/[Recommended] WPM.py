'''[Recommended] WPM'''
def main(choose, wpm):
    '''[Recommended] WPM'''
    if choose == "Kids":
        print(kids(wpm))
    elif choose == "Adults":
        print(adults(wpm))

def kids(wpm):
    '''kids'''
    if wpm < 11:
        return "Very Slow"
    elif 11 <= wpm <= 20:
        return "Slow"
    elif 21 <= wpm <= 30:
        return "Average"
    elif 31 <= wpm <= 40:
        return "Fast"
    else:
        return "Very Fast"

def adults(wpm):
    '''adults'''
    if wpm < 26:
        return "Very Slow"
    elif 26 <= wpm <= 35:
        return "Slow/Beginner"
    elif 36 <= wpm <= 45:
        return "Intermediate/Average"
    elif 46 <= wpm <= 65:
        return "Fast/Advanced"
    elif 66 <= wpm <= 80:
        return "Very Fast"
    else:
        return "Insane"

main(input(), int(input()))

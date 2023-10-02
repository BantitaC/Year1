'''[Midterm 2023] Bad Keyboard'''
def keyboard(txt):
    '''[Midterm 2023] Bad Keyboard'''
    keep = ""

    for i in txt:
        if i == "i":
            keep += "o"
        elif i == "o":
            keep += "i"
        elif i == "I":
            keep += "O"
        elif i == "O":
            keep += "I"
        else:
            keep += i

    print(keep)

keyboard(input())

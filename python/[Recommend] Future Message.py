'''[Recommend] Future Message'''
def future(txt):
    '''[Recommend] Future Message'''
    if txt.isdigit():
        print("Number")
    elif txt.isupper():
        print("Uppercase")
    elif txt.islower():
        print("Lowercase")
    elif txt.istitle():
        print("Title")
    elif txt.isspace():
        print("Space")
    else:
        print("Other")

future(input())

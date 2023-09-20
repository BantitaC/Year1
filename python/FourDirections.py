'''FourDirections'''
def directions(password):
    '''FourDirections'''
    for i in range(len(password)):
        line1()
    print()
    for i in range(len(password)):
        line2(password, i)
    print()
    for i in range(len(password)):
        line3(password, i)
    print()
    for i in range(len(password)):
        line4(password, i)
    print()
    for i in range(len(password)):
        line1()
    print()

def line1():
    '''line1'''
    print("  *  ", end=" ")

def line2(password, num):
    '''line2'''
    if password[num] == "U":
        print(" *** ", end=" ")
    elif password[num] == "D":
        print("  *  ", end=" ")
    elif password[num] == "L":
        print(" *   ", end=" ")
    elif password[num] == "R":
        print("   * ", end=" ")

def line3(password, num):
    '''line3'''
    if password[num] in "UD":
        print("* * *", end=" ")
    elif password[num] in "LR":
        print("*****", end=" ")

def line4(password, num):
    '''line4'''
    if password[num] == "U":
        print("  *  ", end=" ")
    elif password[num] == "D":
        print(" *** ", end=" ")
    elif password[num] == "L":
        print(" *   ", end=" ")
    elif password[num] == "R":
        print("   * ", end=" ")

directions(input())

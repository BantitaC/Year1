'''[Midterm 2020] Pringles'''
def pringles(upside, potatoes, downside, finger):
    '''[Midterm 2020] Pringles'''
    eat = potatoes[:finger]
    potatoincan = potatoes[finger:]
    count = 0
    potatoleft = 0
    for i in eat:
        if i == ")":
            count += 1
    for i in potatoincan:
        if i == ")":
            potatoleft += 1
    print(count)
    if potatoleft == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(upside)
    print(" " * finger + potatoincan)
    print(downside)

pringles(input(), input(), input(), int(input()))

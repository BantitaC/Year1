'''Heads and Legs'''
def rabbitbird(total, leg, rabbit, bird):
    '''Heads and Legs'''
    for i in range(1, total + 1):
        if i % 2 == 0:
            leg -= 4
            rabbit += 1
        else:
            leg -= 2
            bird += 1

    if leg == 0:
        print("%d %d" % (rabbit, bird))
    else:
        print("Impossible")

rabbitbird(int(input()), int(input()), 0, 0)

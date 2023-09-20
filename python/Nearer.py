'''Nearer'''
def nearer(alice, bob, icecream):
    '''Nearer'''
    if abs(alice - icecream) < abs(bob - icecream):
        print("Alice %d" % abs(alice - icecream))
    elif abs(bob - icecream) < abs(alice - icecream):
        print("Bob %d" % abs(bob - icecream))
    else:
        sundae = min(abs(alice-icecream), abs(bob - icecream))
        print("Sundaes %d" % sundae)

nearer(int(input()), int(input()), int(input()))

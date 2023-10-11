'''Tuple's Sad life'''
def sad(num, val):
    '''Tuple's Sad life'''
    amount = num.count(val)
    ind = num.index(val)
    for _ in range(amount):
        for _ in range(amount):
            print(ind, end=" ")
        print()

sad(tuple(input().split()), input())

'''Sequence III'''
def sequence(num):
    '''Sequence III'''
    start = 2
    stop = num+2
    for _ in range(1, num+1):
        for j in range(start, stop):
            print(j, end=" ")
        start += 1
        stop += 1
        print()

sequence(int(input()))

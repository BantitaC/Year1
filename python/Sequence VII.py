'''Sequence VII'''
def sequence(num):
    '''Sequence VII'''
    lst = []
    for i in range(1, num+1):
        lst.append(i)
        for j in range(0, len(lst)):
            print("%d" % lst[j], end=" ")
        print()

    for i in range(num, 0, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()

sequence(int(input()))

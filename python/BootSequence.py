'''BootSequence'''
def sequence(num):
    '''BootSequence'''
    print(*[i for i in range(1, num+1)], sep="_", end="")
sequence(int(input()))

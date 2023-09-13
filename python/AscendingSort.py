'''AscendingSort'''
def ascend():
    '''AscendingSort'''
    thislist = []
    for _ in range(5):
        num = int(input())
        thislist.append(num)
    thislist.sort()
    print(*thislist, sep="\n")
 
ascend()

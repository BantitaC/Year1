'''LineSorting'''
def sorting(line):
    '''LineSorting'''
    lst = []

    for _ in range(line):
        txt = input()
        lst.append(txt)
    lst.sort(key=len)
    print(*lst, sep="\n")

sorting(int(input()))

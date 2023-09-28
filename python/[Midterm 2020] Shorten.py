'''[Midterm 2020] Shorten'''
def short():
    '''[Midterm 2020] Shorten'''
    keep = ""
    start = None
    previous = None
    while True:
        num = int(input())
        if num == -1:
            break
        if start == None:
            start = num
            previous = num
            continue
        else:
            if previous != (num - 1):
                if start == previous:
                    keep += "%d, " % start
                else:
                    keep += "%d-%d, " % (start, previous)
                start = num
                previous = num
            else:
                previous = num
    if start != None:
        if start == previous:
            keep += "%d, " % start
        else:
            keep += "%d-%d, " % (start, previous)
    print(keep.strip(", "))

short()

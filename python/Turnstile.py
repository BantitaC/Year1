'''Turnstile'''
def stile(txt):
    '''Turnstile'''
    count = 0
    lst = []
    lst.append(txt)
    while txt != "END":
        txt = input()
        lst.append(txt)
    for i in range(len(lst)):
        if lst[i] == "C" and lst[i + 1] == "P":
            count += 1
    print(count)

stile(input())

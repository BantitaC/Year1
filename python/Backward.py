'''Backward'''
def backward(txt):
    '''Backward'''
    thislist = []
    while True:
        if txt == "NULL":
            break
        thislist.append(txt)
        txt = input()
    print("\n".join(thislist[::-1]))
 
backward(input())

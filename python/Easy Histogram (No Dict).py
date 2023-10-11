'''Easy Histogram (No Dict)'''
def histogram(txt, keep, nub):
    '''Easy Histogram (No Dict)'''
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in txt:
        if i in alpha:
            keep += i + " = %d" % nub
        if i == i:
            nub += 1
    print(keep, end="")

histogram(input(), "", 0)

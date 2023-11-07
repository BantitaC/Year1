'''[Recommended] Helloooo'''
def hello(txt, keep, count, vowels):
    '''[Recommended] Helloooo'''
    txt = txt[::-1]
    for i in txt:
        if i in vowels:
            count += 1

    for i in txt:
        if i in vowels and count != 0:
            keep += i * 4
            count = 0
        else:
            keep += i
    print(keep[::-1])

hello(input(), "", 0, ['a', 'e', 'i', 'o', 'u'])

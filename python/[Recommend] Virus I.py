'''[Recommend] Virus I'''
def virus(txt, total):
    '''[Recommend] Virus I'''
    for i in txt:
        if i == "o":
            total += 1
    print(total)

virus(input(), 0)

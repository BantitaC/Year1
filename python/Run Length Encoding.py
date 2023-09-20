'''Run Length Encoding'''
def encoding(txt):
    '''Run Length Encoding'''
    count = 1
    encode = ""

    for i in range(1, len(txt)):
        if txt[i] == txt[i - 1]:
            count += 1
        else:
            encode += str(count) + txt[i - 1]
            count = 1
    encode += str(count) + txt[-1]
    print(encode)

encoding(input())

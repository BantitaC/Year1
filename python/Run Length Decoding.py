'''Run Length Decoding'''
def decoding(txt):
    '''Run Length Decoding'''
    count = ""
    result = ""

    for i in txt:
        if i.isnumeric():
            count += i
        elif i.isalpha():
            if count:
                result += i * int(count)
                count = ""
            else:
                result += i
    print(result)

decoding(input())

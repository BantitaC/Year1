'''Helloooo'''
def hello(word, vowels, count, reeverse, result):
    '''Helloooo'''
    for i in word:
        if i in vowels:
            count += 1
    keep = ""
    keep1 = ""
    if count == 0:
        print(word)
    else:
        for j in word[::-1]:
            reeverse += j
        for i in reeverse:
            keep += i
            if i in vowels:
                result += i * 2
            keep += result
            break
        keep1 += reeverse.replace(keep, "")
        keep += keep1
        print(keep[::-1])

hello(input(), ['a', 'e', 'i', 'o', 'u'], 0, "", "")

'''WordSequence II'''
def wordtwo(txt1, txt2):
    '''WordSequence II'''
    for i in range(0, max(len(txt1), len(txt2)) + 1):
        print(txt2[:i] + txt1[i:])

wordtwo(input(), input())

'''Parallelogram'''
def pararell(txt):
    '''Parallelogram'''
    for i in range(len(txt)):
        for j in range(i + 1, len(txt)):
            print(" ", end="")
        for j in range(0, i + 1):
            print(txt[j], end="")
        print()
    for i in range(len(txt) - 1):
        print(txt[i + 1:len(txt)])
    print()

pararell(input())

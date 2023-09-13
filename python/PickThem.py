'''PickThem'''
import json
def pick():
    '''PickThem'''
    num = input()
    numlist = json.loads(num)
    even = 0
    for i in numlist:
        if i % 2 == 0:
            print(i)
            even = 1
    if even == 0:
        print("Nope")
pick()

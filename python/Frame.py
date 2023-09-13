'''Frame'''
def frame(txt):
    '''Frame'''
    print("*" * (len(txt) + 2))
    print("*%s*" % txt)
    print("*" * (len(txt) + 2))
 
frame(input())

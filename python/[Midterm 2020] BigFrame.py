'''[Midterm 2020] BigFrame'''
def bigframe(txt1, txt2, txt3, txt4, txt5):
    '''[Midterm 2020] BigFrame'''
    process = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    print("*" * (process + 4))
    print("* %s" % txt1 + " " * (process - len(txt1)) + " *")
    print("* %s" % txt2 + " " * (process - len(txt2)) + " *")
    print("* %s" % txt3 + " " * (process - len(txt3)) + " *")
    print("* %s" % txt4 + " " * (process - len(txt4)) + " *")
    print("* %s" % txt5 + " " * (process - len(txt5)) + " *")
    print("*" * (process + 4))
 
bigframe(input().rstrip(), input().rstrip(), input().rstrip(), input().rstrip(), input().rstrip())

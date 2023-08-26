'''[Recommend] ValidVar'''
def validvar(num):
    '''[Recommend] ValidVar'''
    reserved_word = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break',\
 'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None']

    for _ in range(num):
        var = input()
        if var in reserved_word:
            print("Invalid")
        elif var.isidentifier():
            print("Valid")
        else:
            print("Invalid")

validvar(int(input()))

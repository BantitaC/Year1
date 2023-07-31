'''Left Arrow'''
def main():
    '''Left Arrow'''
    num1 = int(input())
    num2 = int(input())
    for i in range(num2):
        if i < num2 // 2 + 1:
            space = " " * (num2 // 2 - i)
            star = "*" * num1
        else:
            space = " " * (i - num2 // 2)
            star = "*" * num1
        print(space+star)
main()

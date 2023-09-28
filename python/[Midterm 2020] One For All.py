'''[Midterm 2020] One For All'''
def oneforall(num):
    '''[Midterm 2020] One For All'''
    tmp = ""
    for i in range(1, num + 1):
        name = input()
        if i == num:
            tmp += name + "_" + str(num)
        elif i % 2 != 0:
            tmp += name + ("*" * i)
        else:
            tmp += name + ("-" * i)
    print(tmp)
 
oneforall(int(input()))

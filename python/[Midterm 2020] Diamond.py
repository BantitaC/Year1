'''[Midterm 2020] Diamond'''
def diamond(num):
    '''[Midterm 2020] Diamond'''
    half = num // 2
    for i in range(num):
        for j in range(num):
            if i == half or i + j == half or j - i == half or j == num - i + half - 1 or\
                i - j == half:
                print("*", end="")
            else:
                print(" ", end="")
        print()

diamond(int(input()))

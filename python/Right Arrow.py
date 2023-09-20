'''Right Arrow'''
def arrow(num1, num2):
    '''Right Arrow'''
    mid = num2 // 2
    for i in range(num2):
        if i == 0 or i == num2 - 1:
            print("*" * num1)
        elif i > mid:
            print(" " * (mid - 1) + "*" * num1)
            mid -= 1
        else:
            print(" " * i + "*" * num1)

arrow(int(input()), int(input()))

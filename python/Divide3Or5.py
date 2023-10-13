'''Divide3Or5'''
def divide(num, result):
    '''Divide3Or5'''
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    print(result)

divide(int(float(input())), 0)

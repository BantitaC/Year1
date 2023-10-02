'''Median'''
def main(amount, lst):
    '''Median'''

    for _ in range(amount):
        num = int(input())
        lst.append(num)
    lst.sort()
    if amount % 2 != 0:
        median = int(amount + 1) / 2 - 1
        print("%.1f" % (lst[int(median)]))
    else:
        median1 = int(amount / 2 - 1)
        median2 = int(amount / 2)
        print("%.1f" % ((lst[median1] + lst[median2]) / 2))

main(int(input()), [])

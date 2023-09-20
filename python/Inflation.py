'''Inflation'''
def inflation(num_n, num_k):
    '''Inflation'''
    # keep += (3.81 / 100) * num_n
    for _ in range(num_k):
        num_n = (num_n + (num_n * 381 // 10000))
    print("%d.%02d" % ((num_n // 100), (num_n % 100)))

inflation(int(float(input()) * 100), int(input()))

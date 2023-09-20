'''All_Primes'''
def allprimes(num):
    '''All_Primes'''
    result = 0
    for i in range(1, num+1):
        check = 0
        for j in range(1, i + 1):
            if i == 1 or i == 0:
                check = 0
                break
            if i % j == 0 and j != 1 and j != i:
                check = 0
                break
            else:
                check = 1
        result += check
    print(result)
 
allprimes(int(input()))

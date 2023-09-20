'''isprime_small'''
def prime(num):
    '''isprime_small'''
    check = ""
    for i in range(1, num+1):
        if num == 1 or num == 0:
            print("No")
            break
        elif num % i == 0 and i != 1 and i != num:
            check = "No"
            break
        else:
            check = "Yes"
    print(check)
 
prime(int(input()))

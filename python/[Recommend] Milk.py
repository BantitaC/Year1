'''[Recommend] Milk'''
def milk(num_a, num_b, num_c, num_d):
    '''[Recommend] Milk'''
    milkk = num_d // num_a
    keep = milkk
    while keep >= num_b and num_c != 0:
        if num_b == 0:
            break
        milkk += num_c
        keep += num_c
        keep -= num_b
    print(milkk)

milk(int(input()), int(input()), int(input()), int(input()))

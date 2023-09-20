'''SecondConverter'''
def converter(num_k, num_s, num_m, num_h):
    '''SecondConverter'''
    secondt = num_k % num_s
    minutet = num_k // num_s
    hourt = minutet // num_m
    minutet = minutet % num_m
    hourt = hourt % num_h
    if hourt > num_h:
        hourt = hourt % num_h
    print("%d:%d:%d" % (hourt, minutet, secondt))


converter(int(input()), int(input()), int(input()), int(input()))

'''Regulation'''
def main(int_a, float_b, str_c):
    '''Regulation'''
    print("%30d" % int_a)
    print("%030d" % int_a)
    print("%.2f" % float_b)
    print("%.12f" % float_b)
    print("%40s" % str_c)
main(int(input()), float(input()), str(input()))

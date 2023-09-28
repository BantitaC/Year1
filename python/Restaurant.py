'''Restaurant'''
def restaurant(price_a, price_b, percent_c, plus_d):
    '''Restaurant'''
    # ((a + d) - (c / 100 * (a + d))) - a

    allprice = price_a + plus_d

    if allprice >= price_b:
        allprice = allprice * percent_c
    if price_a >= price_b:
        price_a = price_a * percent_c
    if price_a < allprice:
        print("No %.3f" % (allprice - price_a))
    elif price_a > allprice:
        print("Yes %.3f" % (price_a - allprice))
    else:
        print("Yes")

restaurant(float(input()), float(input()), ((100 - float(input())) / 100), float(input()))

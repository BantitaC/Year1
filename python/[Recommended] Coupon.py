'''[Recommended] Coupon'''
def coupon(price, coupon1, coupon2, discount1, discount2):
    '''[Recommended] Coupon'''
    if price >= float(coupon1[1]):
        discount1 += price - float(coupon1[0])
    else:
        discount1 = 0
    if price >= float(coupon2[1]):
        discount2 += price - ((float(coupon2[0])/100) * price)
    else:
        discount2 = 0
    if discount1 == 0 and discount2 == 0:
        print("Nope")
    elif discount1 < discount2 or discount2 == 0:
        print("1 %.1f" % discount1)
    elif discount2 < discount1 or discount1 == 0:
        print("2 %.1f" % discount2)
    else:
        if float(coupon1[1]) < float(coupon2[1]):
            print("1 %.1f" % discount1)
        elif float(coupon2[1]) < float(coupon1[1]):
            print("2 %.1f" % discount2)
        else:
            print("1 %.1f" % discount1)

coupon(float(input()), input().split(), input().split(), 0, 0)

'''[Recommend] RuleofThree'''
def rule(size, price, weight):
    '''[Recommend] RuleofThree'''
    gram = weight / price
    netprice = price
    netweight = gram

    for _ in range(size-1):
        price = float(input())
        weight = float(input())
        gram = weight / price
        if gram > netweight:
            netprice = price
            netweight = gram
        elif gram == netweight:
            if price < netprice:
                netprice = price
                netweight = gram
        else:
            continue
    print("%.2f %.2f" % (netprice, netweight*netprice))

rule(int(input()), float(input()), float(input()))

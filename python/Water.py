'''Water'''
def water(month, price, amount, priceplus, freeuse):
    '''Water'''
    free = 0
    for _ in range(month):
        use = float(input())

    if use > amount:
        result = (use * price) + ((use - amount) * priceplus)

water(int(input()), float(input()), float(input()), float(input()), float(input()))

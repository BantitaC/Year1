'''Coke V2'''
def coke(oldprice, exchange, newprice, want):
    '''Coke'''
    price = oldprice * want
    if exchange == 0:
        print(price)
    else:
        discount = int((want - 1) / exchange)
        price = (discount * newprice) + ((want - discount) * oldprice)
        print(price)

coke(int(input()), int(input()), int(input()), int(input()))

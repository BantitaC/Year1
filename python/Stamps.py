'''Stamps'''
def stamps():
    '''Stamps'''
    timetoeat = int(input())
    billtostamp = int(input())
    stampup = int(input())
    sasomtopro = int(input())
    pro = int(input())
    mystamp = 0
    mybill = 0
    for _ in range(timetoeat):
        price = int(input())
        if mystamp >= sasomtopro:
            #rounddis lod ki rob
            rounddis = price // pro
            if price % pro > 0:
                rounddis += 1
            tmp = mystamp // sasomtopro
            can = min(rounddis, tmp)
            if can > 0:
                price -= can * pro
                price = max(price, 0)
                mystamp -= can * sasomtopro
        if price >= billtostamp:
            mystamp += (price//billtostamp)*stampup
        mybill += price
    print(mybill)
    print(mystamp)

stamps()

'''[Recommend] ProgressiveTax'''
def taxx():
    '''[Recommend] ProgressiveTax'''
    money = int(input())
    tax = 0
    if money >= 4000000:
        tmp = money - 4000000
        money -= tmp
        tax += tmp*0.35
    if money > 2000000:
        tmp = money - 2000000
        money = 2000000
        tax += tmp*0.30
    if money > 1000000:
        tmp = money - 1000000
        money -= tmp
        tax += tmp*0.25
    if money > 750000:
        tmp = money - 750000
        money -= tmp
        tax += tmp*0.20
    if money > 500000:
        tmp = money - 500000
        money -= tmp
        tax += tmp*0.15
    if money > 300000:
        tmp = money - 300000
        money -= tmp
        tax += tmp*0.10
    if money > 150000:
        tmp = money - 150000
        money -= tmp
        tax += tmp*0.05
    if money > 0:
        tax += 0
    print(int(tax))

taxx()

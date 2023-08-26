'''[Recommend] Bill'''
def bill(menu):
    '''[Recommend] Bill'''
    service_charge = (10 / 100) * menu

    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000

    vat = (7 / 100) * (menu + service_charge)

    print("%.2f" % (menu + service_charge + vat))

bill(int(input()))

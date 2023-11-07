'''BTU'''
def main(area, height, people, roomtype, sun):
    '''BTU'''
    btu = plus(area)

    if height > 8:
        btu += ((height - 8) * 1000)

    if people > 2:
        btu += ((people - 2) * 600)

    if roomtype == "kitchen":
        btu += 4000

    if sun == "facing the sun":
        btu += ((10 / 100) * btu)
    elif sun == "shaded":
        btu -= ((10 / 100) * btu)

    print(int(btu))

def tablebtu(area):
    '''table1'''
    if area >= 100 and area <= 150:
        return 5000
    elif area > 150 and area <= 250:
        return 6000
    elif area > 250 and area <= 300:
        return 7000
    elif area > 300 and area <= 350:
        return 8000
    elif area > 350 and area <= 400:
        return 9000
    elif area > 400 and area <= 450:
        return 10000
    elif area > 450 and area <= 550:
        return 12000

def tablebtu2(area):
    '''table2'''
    if area > 550 and area <= 700:
        return 14000
    elif area > 700 and area <= 1000:
        return 18000
    elif area > 1000 and area <= 1200:
        return 21000
    elif area > 1200 and area <= 1400:
        return 23000
    elif area > 1400 and area <= 1500:
        return 24000
    elif area > 1500 and area <= 2000:
        return 30000
    elif area > 2000 and area <= 2500:
        return 34000

def plus(area):
    '''plus'''
    if area <= 550:
        return tablebtu(area)
    else:
        return tablebtu2(area)

main(int(input()), int(input()), int(input()), input(), input())

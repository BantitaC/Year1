'''[Recommend] Stair'''
def stair(height, amount):
    '''[Recommend] Stair'''
    three = 0
    cal = 0
    out = 0
    for _ in range(amount):
        height1 = int(input())
        cal = height1 + cal
        if height1 > height:
            out = 1
        elif cal == height:
            three += 1
            cal = 0
        elif cal > height:
            three += 1
            cal = height1
    if cal > 0:
        three += 1
    if out == 1:
        print("NO")
    else:
        print(three)

stair(int(input()), int(input()))

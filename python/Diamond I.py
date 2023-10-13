'''Diamond I'''
def diamond(deep, width, dia, val):
    '''Diamond I'''
    for _ in range(deep):
        value = input().split()
        dia.append(value)
    for i in range(width):
        cal = 0
        for j in dia:
            cal += int(j[i])
        val.append(cal)
    print(max(val))

diamond(int(input()), int(input()), [], [])

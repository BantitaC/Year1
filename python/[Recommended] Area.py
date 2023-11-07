'''[Recommended] Area'''
def area(num, keep, count):
    '''[Recommended] Area'''
    for _ in range(num):
        spe = input()
        keep += spe
    for i in keep:
        if i.isspace():
            count += 0
        else:
            count += 1
    print(count)

area(int(input()), '', 0)

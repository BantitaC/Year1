'''ball'''
def ball(height):
    '''ball'''
    cen = height * 100
    count = 0
    while cen >= 1:
        cen = cen * (3/5)
        count += 1
    print(int(count - 1))
 
ball(float(input()))

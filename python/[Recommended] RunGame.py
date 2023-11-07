'''[Recommended] RunGame'''
def run(position, distance, keep):
    '''[Recommended] RunGame'''
    for i in position:
        distance = abs(int(i) - distance)
        keep += distance
        distance = int(i)
    print(keep)

run(input().split(), 0, 0)

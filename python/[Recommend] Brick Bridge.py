'''[Recommend] Brick Bridge'''
def brick(small, large, goal):
    '''[Recommend] Brick Bridge'''
    lll = goal // 5
    if goal < small or small == goal:
        print(goal)
    else:
        print(-1)
 
brick(int(input()), int(input()), int(input()))
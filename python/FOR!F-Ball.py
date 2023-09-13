'''FOR!F-Ball'''
def forif(choose):
    '''FOR!F-Ball'''
    ball = 1
    for move in choose:
        if move == "A":
            if ball == 1:
                ball = 2
            elif ball == 2:
                ball = 1
        elif move == "B":
            if ball == 2:
                ball = 3
            elif ball == 3:
                ball = 2
        elif move == "C":
            if ball == 1:
                ball = 3
            elif ball == 3:
                ball = 1
    print(ball)
 
forif(input())

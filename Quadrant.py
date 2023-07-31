'''Quadrant'''
def quadrant(num_x, num_y):
    '''mark on the Quadrant'''
    if num_x == 0 and num_y == 0:
        print("O")
    elif num_y == 0 and num_x != 0:
        print("X")
    elif num_x == 0 and num_y != 0:
        print("Y")
    elif num_x > 0 and num_y > 0:
        print("Q1")
    elif num_x < 0 and num_y > 0:
        print("Q2")
    elif num_x < 0 and num_y < 0:
        print("Q3")
    elif num_x > 0 and num_y < 0:
        print("Q4")
quadrant(int(input()), int(input()))

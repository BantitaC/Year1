'''ChristmasTree'''
def tree(numn, numk):
    '''ChristmasTree'''
    for i in range(1, numn + 1):
        print(" " * (numn - i) + "*" * (2 * i -1))
    for i in range(numk):
        print(" " * (numn - 2) + "-" * 3)
 
tree(int(input()), int(input()))

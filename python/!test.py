'''sequence 6'''
def sequence(num):
    '''งง'''
    for row in range(num):
        for col in range(num):
            if col == 0:
                space = " "
                print("*"+space, end="")
        print(" ")

sequence(5)

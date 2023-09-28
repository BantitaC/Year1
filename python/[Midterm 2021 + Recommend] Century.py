'''[Midterm 2021 + Recommend] Century'''
import math
def century(num):
    '''[Midterm 2021 + Recommend] Century'''
    for _ in range(num):
        year = input()
        if year.count("B.E."):
            delete = year.strip("B.E. ")
            new = int(delete) - 543
            if new < 0:
                print("ERROR")
            else:
                print(math.ceil((int(delete) - 543) / 100))
        elif year.count("A.D."):
            delete = year.strip("A.D. ")
            print(math.ceil(int(delete) / 100))
        else:
            print("ERROR")

century(int(input()))

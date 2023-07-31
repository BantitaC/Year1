'''MyMath'''
import math
def mymath():
    '''MyMath'''
    ans_1 = ((math.sin(math.radians(90)))+(math.sin(math.radians(60)))**2)
    ans_2 = ((math.cos(math.radians(245**2)))+(math.cos(math.radians(45+135))))
    print(ans_1 / ans_2)
    print((math.factorial(16)*math.factorial(4))/math.factorial(8))
    print((15+25)/(((25-12)**2)+((12-15)**2))**0.5)
    print(math.log(1234**4, 10))
    ans_1 = (math.log(4234, 5) + math.log2(8191) + math.log10(156154**71))
    ans_2 = (math.log(777, 7) - math.log(888, 8) - math.log(999, 9))
    print(ans_1 / ans_2)
mymath()

'''[Recommend + Midterm 2021] Cha Cha Cha'''
import math
def cha(day):
    '''[Recommend + Midterm 2021] Cha Cha Cha'''
    count = 0
    for _ in range(day):
        hour = math.ceil(float(input()))
        count += (8720 * hour)
    print(int(count))
 
cha(int(input()))

'''[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย'''
import math
 
def saitama(pushup, situp, updown, run):
    '''[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย'''
    day_pushup = int(input())
    day_situp = int(input())
    day_run = int(input())
    day_updown = int(input())
 
    day_pushup = pushup / day_pushup
    day_situp = situp / day_situp
    day_updown = updown / day_updown
    day_run = run / day_run
 
    cal = findmx(day_pushup, day_situp)
    cal = findmx(cal, day_updown)
    cal = findmx(cal, day_run)
 
    print(math.ceil(cal))
 
def findmx(num1, num2):
    '''find max'''
    if num1 > num2:
        return num1
    return num2
 
saitama(int(input()), int(input()), int(input()), int(input()))

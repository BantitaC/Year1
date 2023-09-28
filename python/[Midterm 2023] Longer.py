'''[Midterm 2023] Longer'''
import math

def longer(radius, width, length):
    '''[Midterm 2023] Longer'''
    circle = 2 * math.pi * radius
    rec = 2 * (width + length)
    if circle > rec:
        print("Circle is longer")
        print("%.5f" % (circle - rec))
    elif rec > circle:
        print("Rectangle is longer")
        print("%.5f" % (rec - circle))
    else:
        print("Equal")
        print("%.5f" % (circle - rec))

longer(float(input()), float(input()), float(input()))

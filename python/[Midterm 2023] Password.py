'''[Midterm 2023] Password'''
import math

def main(password):
    '''[Midterm 2023] Password'''
    atoz, capital, num, printable = 26, 26, 10, 32

    if password.isalpha():
        if password.islower():
            pool += atoz
        if password.isupper():
            pool += capital
    elif password.isalnum():
        pool += (atoz + num)
    entropy = math.log2(pool**(len(password)))

main(input())

'''[Midterm 2023] Niwarn World'''
import math

def niwarn(num_n, num_s, num_k):
    '''[Midterm 2023] Niwarn World'''
    f_x = 2 + (math.log2(num_n ** 2) / ((2 * num_n) * math.log2(num_n)))

    f_y = (math.sin(math.radians(30)) + ((2 * num_s) ** 0.5)) / (f_x + 3)

    fyz = ((math.sin(math.radians(30)) + ((2 * num_k) ** 0.5)) / ((2 + (math.log2(num_k ** 2) / \
((2 * num_k) * math.log2(num_k)))) + 3)) ** 2

    fxz = (2 + (math.log2(num_k ** 2) / ((2 * num_k) * math.log2(num_k)))) ** 4

    f_z = fyz + ((8456 * fxz) / (24 * num_k))

    print("X: %.1f, Y: %.1f, Z: %.1f" % (f_x, f_y, f_z))

niwarn(float(input()), float(input()), float(input()))

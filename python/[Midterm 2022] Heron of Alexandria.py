'''[Midterm 2022] Heron of Alexandria'''
def heron(numa, numb, numc):
    '''[Midterm 2022] Heron of Alexandria'''
    num_s = (numa + numb + numc) / 2
    print("%.3f" % (((num_s * (num_s - numa)) * (num_s - numb) * (num_s - numc)) ** 0.5))
 
heron(float(input()), float(input()), float(input()))

'''GraderMachine'''
def grader(first, last):
    '''GraderMachine'''
    total = 0
    for i in range(first, last+1, 1):
        if i % 2 == 0:
            total += i
    print("pass : %d" % i)
    print("Sum : %d" % total)
grader(int(input()), int(input()))

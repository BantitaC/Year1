'''[Midterm 2023] Lift'''
def lift(people, macweight, cal, kid, adult):
    '''[Midterm 2023] Lift'''

    for _ in range(people):
        age = int(input())
        weight = float(input())
        cal += weight
        if age >= 12:
            adult += 1
        else:
            kid += 1

    if kid >= 1 and adult == 0:
        print("Not Safe")
    elif cal > macweight:
        print("Not Safe")
    else:
        print("Safe")

lift(int(input()), float(input()), 0, 0, 0)

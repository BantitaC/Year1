'''[Midterm 2023] Lift'''
def lift(people, macweight, safe, cal):
    '''[Midterm 2023] Lift'''

    for _ in range(people):
        age = int(input())
        weight = float(input())
        cal += weight
        if age >= 12:
            safe = 1
            if cal <= macweight:
                safe = 1
            else:
                safe = 0
            continue
        else:
            safe = 0

    if safe == 1:
        print("Safe")
    elif safe == 0:
        print("Not Safe")

lift(int(input()), float(input()), 0, 0)

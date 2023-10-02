'''[Midterm 2023] Home Run'''
def homerun(sanarm, distance):
    '''[Midterm 2023] Home Run'''
    count = 0

    for _ in range(sanarm):
        length = float(input())
        if distance > length:
            count += 1
    print(count)

homerun(int(input()), float(input()))

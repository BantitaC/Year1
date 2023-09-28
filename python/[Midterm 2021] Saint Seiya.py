'''[Midterm 2021] Saint Seiya'''
def seiya(second, punch):
    '''[Midterm 2021] Saint Seiya'''
    punchh = 0

    for i in range(2, second + 1, 2):
        if punchh < punch:
            if i % 6 == 0:
                punchh += 1
            elif i % 2 == 0:
                punchh += 165
        else:
            punchh += (second + 1 - i) * 12
            break
    print(punchh)

seiya(int(input()), int(input()))

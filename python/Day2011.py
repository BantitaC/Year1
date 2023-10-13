'''Day2011'''
def day2021(date, month, week, datemonth):
    '''Day2011'''
    total = sum(datemonth[1:month]) + date
    index = total % 7
    week = week[index]

    return week

result = day2021
print(result)

day2021(int(input()), int(input()), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'\
, 'Saturday', 'Sunday'], [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

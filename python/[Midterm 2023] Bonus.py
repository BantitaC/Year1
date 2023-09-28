'''[Midterm 2023] Bonus'''
def main(salary, year, month):
    '''[Midterm 2023] Bonus'''
    if month >= 10:
        year += 1

    if year >= 1:
        if year > 20:
            year = 20
            bonus = salary * year
            if bonus > 1000000:
                bonus = 1000000
            elif bonus < 5000:
                bonus = 5000
        else:
            bonus = salary * year
            if bonus > 1000000:
                bonus = 1000000
            elif bonus < 5000:
                bonus = 5000
    else:
        bonus = salary * year
        if bonus < 5000:
            bonus = 5000
    print(bonus)

main(int(input()), int(input()), int(input()))

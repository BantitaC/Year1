'''[Midterm 2022] Netflix'''
def package(premium, standard, basic, mobile, total):
    """Package Functions"""
    if premium > 0:
        print("Premium x %d" % premium)
    if standard > 0:
        print("Standard x %d" % standard * (standard > 0))
    if basic > 0:
        print("Basic x %d" % basic * (basic > 0))
    if mobile > 0:
        print("Mobile x %d" % mobile * (mobile > 0))
    print("Total = %d THB" % total)

def netflix(screens, devices):
    '''[Midterm 2022] Netflix'''
    input()
    input()
    laptoptv, hd_, ultrahd = input(), input(), input()

    count_premium, count_standard, count_basic, count_mobile, total = 0, 0, 0, 0, 0

    while screens > 0 or devices > 0:
        if (ultrahd == "Yes" or hd_ == "Yes" or laptoptv == "Yes") \
        and (screens >= 3 or devices >= 3):
            total += 419
            count_premium += 1
            screens -= 4
            devices -= 4
        elif (hd_ == "Yes" or laptoptv == "Yes") \
        and (screens >= 2 or devices >= 2):
            total += 349
            count_standard += 1
            screens -= 2
            devices -= 2
        elif laptoptv == "Yes" and ultrahd == "No" and hd_ == "No":
            total += 279
            count_basic += 1
            screens -= 1
            devices -= 1
        else:
            if ultrahd == "Yes":
                total += 419
                count_premium += 1
                screens -= 4
                devices -= 4
            elif hd_ == "Yes":
                total += 349
                count_standard += 1
                screens -= 2
                devices -= 2
            elif laptoptv == "Yes":
                total += 279
                count_basic += 1
                screens -= 1
                devices -= 1
            else:
                total += 99
                count_mobile += 1
                screens -= 1
                devices -= 1
    package(count_premium, count_standard, count_basic, count_mobile, total)

netflix(int(input()), int(input()))

'''WeightStation'''
def station(average, point_1, point_2, point_3):
    '''WeightStation'''

    point_4 = (average * 4) - (point_1 + point_2 + point_3)
    total = average * 4
    average_weight = total / 4

    if total > 15000:
        print("Overweight")
    elif abs(average - point_1) > average_weight / 2 or \
    abs(average - point_2) > average_weight / 2 or \
    abs(average - point_3) > average_weight / 2 or \
    abs(average - point_4) > average_weight / 2:
        print("Unbalance")
    else:
        print("Pass %.2f" % point_4)

station(float(input()), float(input()), float(input()), float(input()))

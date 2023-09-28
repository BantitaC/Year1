'''Kaprekars'''
def kaprekars(num):
    '''Kaprekars'''
    count = 0
    while True:
        if num == 6174:
            break
        else:
            num = int(moreless(num, "More")) - int(moreless(num, "Less"))
            if len(str(num)) < 4:
                num = str(num) + "0" * (4 - len(str(num)))
            count += 1
    print(count)

def moreless(num, txt):
    '''moreless'''
    count1 = str(num).count("1")
    count2 = str(num).count("2")
    count3 = str(num).count("3")
    count4 = str(num).count("4")
    count5 = str(num).count("5")
    count6 = str(num).count("6")
    count7 = str(num).count("7")
    count8 = str(num).count("8")
    count9 = str(num).count("9")
    count0 = str(num).count("0")
    if txt == "More":
        return "9" * count9 + "8" * count8 + "7" * count7\
+ "6" * count6 + "5" * count5 + "4" * count4 + "3" * count3\
+ "2" * count2 + "1" * count1 + "0" * count0
    if txt == "Less":
        return "0" * count0 + "1" * count1 + "2" * count2\
+ "3" * count3 + "4" * count4 + "5" * count5 + "6" * count6\
+ "7" * count7 + "8" * count8 + "9" * count9

kaprekars(input())

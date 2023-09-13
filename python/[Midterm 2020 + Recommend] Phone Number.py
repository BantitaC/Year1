""" Phone Number"""
def phone():
    """ Phone Number"""
    phone_num = input()
    pattern = input()
    if pattern == "Domestic":
        if len(phone_num) == 9:
            print(phone_num[0], phone_num[1:5], phone_num[5:9])
        elif len(phone_num) == 10:
            print(phone_num[:2], phone_num[2:6], phone_num[6:10])
    elif pattern == "International":
        if len(phone_num) == 9:
            print("+66", phone_num[1:5], phone_num[5:9])
        elif len(phone_num) == 10:
            print("+66" + phone_num[1], phone_num[2:6], phone_num[6:10])
 
phone()

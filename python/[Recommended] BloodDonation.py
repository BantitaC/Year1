'''[Recommended] BloodDonation'''
def donation(age, weight, amount, book):
    '''[Recommended] BloodDonation'''
    if 17 <= age <= 70 and weight >= 45:
        if 17 < age < 60:
            if (amount == 0 and age <= 55) or amount > 0:
                print("Yes")
            else:
                print("No")
        elif age == 17 or age >= 60:
            book = input()
            if book == "True":
                if (amount == 0 and age <= 55) or amount > 0:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

donation(int(input()), int(input()), int(input()), "False")

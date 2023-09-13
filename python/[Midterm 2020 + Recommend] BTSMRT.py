"""BTSMRT"""
def main():
    """BTSMRT"""
    festi = input()
    age = float(input())
    height = float(input())
    if festi == "Children Day":
        if age < 14 and height <= 140:
            print("FREE")
        else:
            print("PAY")
    elif festi == "Senior Day":
        if (age >= 60) or (age < 14 and height < 90):
            print("FREE")
        else:
            print("PAY")
    elif festi == "Normal Day":
        if age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
 
main()

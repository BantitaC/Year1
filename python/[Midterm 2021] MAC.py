'''[Midterm 2021] MAC'''
def mac(address):
    '''[Midterm 2021] MAC'''
    charactor = "ABCDEFabcdef0123456789.:-"

    if not (len(address) == 17 or len(address) == 14):
        return print("ERROR")
    for i in address:
        if i not in charactor:
            return print("ERROR")
    if not (address.count(":") == 5 or address.count(".") == 2 or address.count("-") == 5):
        return print("ERROR")
    elif address[2] == ":" and address[5] == ":" and address[8] == ":" and \
address[11] == ":" and address[14] == ":":
        print("VALID 2")
    elif address[2] == "-" and address[5] == "-" and address[8] == "-" and \
address[11] == "-" and address[14] == "-":
        print("VALID 1")
    elif address[4] == "." and address[9] == "." and address[:4].isalnum() and \
address[5:9].isalnum() and address[10:].isalnum():
        print("VALID 3")
    else:
        print("ERROR")

mac(input())

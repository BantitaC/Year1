'''[Midterm 2021] iPhone 13 Again'''
def iphone(serie, size):
    '''[Midterm 2021] iPhone 13 Again'''
    if serie == "iPhone 13 mini":
        print(mini(serie, size))
    elif serie == "iPhone 13":
        print(sibsam(serie, size))
    elif serie == "iPhone 13 Pro":
        print(pro(serie, size))
    elif serie == "iPhone 13 Pro Max":
        print(promax(serie, size))
    else:
        print("Not Available")
 
def mini(serie, size):
    '''iPhone 13 mini'''
    if serie == "iPhone 13 mini":
        if size == "128 GB":
            return 25900
        elif size == "256 GB":
            return 29900
        elif size == "512 GB":
            return 37900
        else:
            return "Not Available"
 
def sibsam(serie, size):
    '''iPhone 13'''
    if serie == "iPhone 13":
        if size == "128 GB":
            return 29900
        elif size == "256 GB":
            return 33900
        elif size == "512 GB":
            return 41900
        else:
            return "Not Available"
 
def pro(serie, size):
    '''iPhone 13 Pro'''
    if serie == "iPhone 13 Pro":
        if size == "128 GB":
            return 38900
        elif size == "256 GB":
            return 42900
        elif size == "512 GB":
            return 50900
        elif size == "1 TB":
            return 58900
        else:
            return "Not Available"
 
def promax(serie, size):
    '''iPhone 13 Pro Max'''
    if serie == "iPhone 13 Pro Max":
        if size == "128 GB":
            return 42900
        elif size == "256 GB":
            return 46900
        elif size == "512 GB":
            return 54900
        elif size == "1 TB":
            return 62900
        else:
            return "Not Available"
 
iphone(input(), input())

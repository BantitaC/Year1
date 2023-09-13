"""PickThemAgain"""
def pick():
    """PickThemAgain"""
    num = input().split()
    numlist = [int(item) for item in num]
    odd = []
    ood = 0
    for i in numlist:
        if i % 3 == 0 or i % 5 == 0:
            odd.append(i)
            ood = 1
    if ood == 0:
        print("Nope")
    else:
        print(*odd[::-1], sep="\n")
 
pick()

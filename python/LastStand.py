"""LastStand"""
import json
def stand():
    """LastStand"""
    num = input()
    numlist = json.loads(num)
    for num in numlist:
        num = str(num)
        print(num[-1])
 
stand()

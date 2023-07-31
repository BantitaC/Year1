'''DataSpike'''
def data():
    '''DataSpike'''
    data1 = int(input())
    data2 = int(input())
    data3 = int(input())
    data4 = int(input())
    data5 = int(input())
    data6 = int(input())
    data7 = int(input())
    data8 = int(input())

    cal1 = find(data1, data2)
    cal2 = find(cal1, data3)
    cal3 = find(cal2, data4)
    cal4 = find(cal3, data5)
    cal5 = find(cal4, data6)
    cal6 = find(cal5, data7)
    cal7 = find(cal6, data8)
    print(cal7)

def find(num1, num2):
    '''find maximum'''
    if num1 > num2:
        return num1

data()

'''Key'''
def key(idnum):
    '''Key'''
    key1 = 0
    for i in range(len(idnum)):
        key1 += int(idnum[i])
    key2 = int(idnum[-3:]) * 10
    sumkey = key1 + key2
    if sumkey < 1000:
        sumkey += 1000
    print(str(sumkey)[-4:])
 
key(input())

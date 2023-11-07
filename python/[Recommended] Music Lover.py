'''[Recommended] Music Lover'''
def mslover(amount):
    '''[Recommended] Music Lover'''
    lstmusic = {}
    for i in range(amount):
        music = input().strip().split("-")
        if music[0] not in lstmusic:
            lstmusic[music[0]] = [music[1]]
        else:
            lstmusic[music[0]].append(music[1].strip())

    for key, value in lstmusic.items():
        print(key)
        for i in value:
            print(i)

mslover(int(input()))

import json
'''[Recommended] Difference'''
def diff(count, keep, keep1):
    '''[Recommended] Difference'''
    txt1 = input()
    txt2 = input()
    txtlist = json.loads(txt1)
    txtlist2 = json.loads(txt2)
    txtlist.sort()
    txtlist2.sort()
    # i = txtlist if len(txtlist) > len(txtlist2) else txtlist2
    
    # for j in i:
    #     if j == txtlist2[0]:
    #         txtlist2 = txtlist2[1::]
    #         print(txtlist2)
    for i in txtlist:
        if i in txtlist2:
            
        else:
            keep.append(i)
            count += 1
    print(keep, count)

diff(0, [], [])

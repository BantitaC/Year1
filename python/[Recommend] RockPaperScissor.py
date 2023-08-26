'''[Recommend] RockPaperScissor'''
def rps(game, awin, bwin):
    '''[Recommend] RockPaperScissor'''
    for i in range(2, len(game) + 1, 2):
        separate = game[i-2:i]

        if separate == "RS" or separate == "SP" or separate == "PR":
            awin += 1
        elif separate == "RP" or separate == "SR" or separate == "PS":
            bwin += 1
        elif separate == "RR" or separate == "SS" or separate == "PP":
            awin += 0.
            bwin += 0

    if awin > bwin:
        print("A win %d-%d" % (awin, bwin))
    elif bwin > awin:
        print("B win %d-%d" % (bwin, awin))
    else:
        print("DRAW", awin)

rps(input(), 0, 0)

'''[Recommend] Elo'''
def elo(v_ra, v_rb, txtab):
    '''[Recommend] Elo'''
    e_a = 1 / (1 + (10 ** ((v_rb - v_ra) / 400)))
    e_b = 1 / (1 + (10 ** ((v_ra - v_rb) / 400)))

    if txtab == "A":
        print("%.2f" % e_a)
    elif txtab == "B":
        print("%.2f" % e_b)

elo(int(input()), int(input()), input())

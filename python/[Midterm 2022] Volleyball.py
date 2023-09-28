'''[Midterm 2022] Volleyball'''
def win(win_team_a, win_team_b, value):
    '''winner'''
    return win_team_a >= value or win_team_b >= value

def notdeal(win_team_a, win_team_b):
    '''not deal mode'''
    return abs(win_team_a - win_team_b) >= 2

def volleyball(txt):
    '''[Midterm 2022] Volleyball'''
    win_team_a = 0
    win_team_b = 0
    round_team_a = 0
    round_team_b = 0
    str_builder = ""
    increment = 0
    finished = False

    while len(txt) != 0:
        for text in txt:
            if win(win_team_a, win_team_b, 25) \
            and notdeal(win_team_a, win_team_b) and increment <= 3:
                finished = True
                break
            if win(win_team_a, win_team_b, 15) \
            and notdeal(win_team_a, win_team_b) and increment == 4:
                finished = True
                break
            if text == "A":
                win_team_a = win_team_a + 1
            elif text == "B":
                win_team_b = win_team_b + 1
            str_builder = str_builder + text
        increment = increment + 1
        if win_team_a > win_team_b:
            round_team_a = round_team_a + 1
        else:
            round_team_b = round_team_b + 1
        if increment <= 5:
            print("Set %d: A (%d) | B (%d)" % (increment, win_team_a, win_team_b))
        txt = txt.replace(str_builder, "", 1)
        if increment >= 4 and finished and round_team_a - round_team_b != 0 \
        or (abs(round_team_a - round_team_b) == 3):
            print("A won %d:%d set"\
                % (round_team_a, round_team_b) * (round_team_a > round_team_b) + \
                "B won %d:%d set"\
                % (round_team_b, round_team_a) * (round_team_a < round_team_b))
            break

        # set default
        finished = False
        win_team_a = 0
        win_team_b = 0
        str_builder = ""
    if not finished:
        print("The game has not finished yet.")

volleyball(input() + " ")

'''[Midterm 2021] Solar System'''
def solar(sunnplanet):
    '''[Midterm 2021] Solar System'''
    tmp, hot, cold, left_star, right_star = tmpdata(sunnplanet, ""), "", "", None, None
    buffer, n_star, prev, prev_star, sun = "", 0, -1, "", 0

    for i in tmp:
        if i == " ":
            n_star += 1
            current = sunnplanet[prev + 1:int(buffer)]
            if left_star is None:
                left_star = current + " "
            if current == "Sun":
                hot += prev_star + " "
                sun = n_star
            if prev_star == "Sun":
                hot += current
            prev, prev_star = int(buffer), current
            buffer = " "
        elif i.isnumeric():
            buffer += str(i)
    if right_star is None:
        right_star = prev_star
    if sunnplanet.strip() != "Sun":
        if abs(1 - sun) > abs(n_star - sun):
            cold = left_star
        elif abs(1 - sun) == abs(n_star - sun):
            cold = left_star + right_star
        else:
            cold = right_star
    print("Hot: %s\nCool: %s" % (hot.strip(), cold.strip()))

def tmpdata(txt, tmp):
    '''Temp Data'''
    for i, j in enumerate(txt):
        if i > 2 and txt[i - 3] + txt[i - 2] + txt[i - 1] + j == "Sun ":
            tmp += str(i) + " "
        elif j == " " and txt[i - 3] + txt[i - 2] + txt[i - 1] + j != "Sun ":
            tmp += str(i) + " "
    return tmp

solar(input() + " ")

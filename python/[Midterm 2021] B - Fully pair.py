'''[Midterm 2021] B - Fully pair?'''
def pair(alphabet):
    '''[Midterm 2021] B - Fully pair?'''
    keep = ""
    none = ""
    count = 0
    for i in alphabet:
        if keep.count(i) <= 0:
            keep += i
    for i in keep:
        if alphabet.count(i) % 2 != 0:
            none += i
            count += 1
    if count == 0:
        print("fully paired")
    else:
        print(none)

pair(input().lower())

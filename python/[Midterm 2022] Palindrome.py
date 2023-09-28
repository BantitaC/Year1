'''[Midterm 2022] Palindrome'''
def palindrome(num, time):
    '''[Midterm 2022] Palindrome'''
    keep = 0

    while keep != num:
        val_x = "%02d" % (int(time[-2:]) + 1)
        hours = time[0:2].replace(":", "")
        if int(val_x) % 60 == 0 and int(val_x) != 0:
            val_x = "00"
            val_y = int(hours) + 1
            hours = str(val_y)
        if int(hours) % 24 == 0:
            hours = "0"
        time = hours + ":" + val_x
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            keep += 1
            print(time)

palindrome(int(input()), input())

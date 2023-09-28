'''[Midterm 2020] Ping'''

def time(line):
    '''Get MS'''
    if line.count("gettime="):
        start = line.find("gettime=")
        end = line.find("ms")
        return int(line[start + 5:end])
    return "Nofound"

def pingg():
    '''[Midterm 2020] Ping'''
    ping = input()
    input()
    line1 = input()
    line2 = input().replace("<1", "=0")
    line3 = input().replace("<1", "=0")
    line4 = input().replace("<1", "=0")
    line5 = input().replace("<1", "=0")
    ip_ = ""

    if not ping[ping.find("ping ") + 5:][0].isdigit():
        f_ip = line1.find("[")
        b_ip = line1.find("]")
        ip_ = line1[f_ip + 1:b_ip]
    else:
        ip_ = ping[ping.find("ping ") + 5:]
    success = (line2 + line3 + line4 + line5).count(ip_)
    print("Ping statistics for %s:" % (ip_))
    print("    Packets: Sent = 4, Recieved = %d, Lost = %d (%s)," %
        (success, 4 - success, str((4 - success) * 25) + "% loss"))
    timee = [time(line2), time(line3), time(line4), time(line5)]
    for _ in range(timee.count("Nofound")):
        timee.remove("Nofound")
    if len(timee):
        print("Approximate round trip times in milli-seconds:")
        maxx = max(timee)
        minn = min(timee)
        average = int(sum(timee) / len(timee))
        print("""    Minimum = %dms, Maximum = %dms, Average = %dms""" % (minn, maxx, average))

pingg()

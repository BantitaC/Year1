'''[Recommended] OTP'''
def onetime():
    '''[Recommended] OTP'''
    lstcount = []
    while True:
        lstcount = []
        otp = input()
        if otp == '0':
            break
        # lstcount = [otp.count(str(i)) for i in range(10)]
        for i in range(10):
            lstcount.append(otp.count(str(i)))
        if len(otp) == 4 and lstcount.count(2) == 1:
            print("Valid")
        elif len(otp) == 6 and lstcount.count(2) == 2 or lstcount.count(3) == 1:
            print("Valid")
        elif len(otp) == 8 and lstcount.count(3) == 2 or lstcount.count(2) == 3:
            print("Valid")
        else:
            print("Invalid")

onetime()

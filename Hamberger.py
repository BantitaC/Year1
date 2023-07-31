'''Hamberger'''
def main():
    '''Hamberger'''
    breadl = int(input())
    breadr = int(input())
    bread = "|"
    pork = "*"
    print(bread*breadl + pork*(breadl*2) + pork*(breadr*2) + bread*breadr)
main()

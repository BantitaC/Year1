'''Hamburger'''
def hamburger(breadl, breadr):
    '''Hamburger'''
    print("|" * breadl + "*" * ((breadr + breadl) * 2) + "|" * breadr)
 
hamburger(int(input()), int(input()))
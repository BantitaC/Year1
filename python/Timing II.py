'''Timing II'''
def timing(seconds):
    '''Timing II'''
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24
    if days < 10000:
        print("%04d:" %days + "%02d:" %hours + "%02d:" %minutes + "%02d" %seconds)
    else:
        print("ERR_:__:__:__")
timing(int(input()))

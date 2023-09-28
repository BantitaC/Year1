'''[Midterm 2022] Meteorite'''
def meteorite(weight, piece, ckilo):
    '''[Midterm 2022] Meteorite'''
    meteo = 1
    shoot = 0
    while weight >= ckilo:
        shoot += meteo
        meteo = piece * meteo
        weight /= piece
    print(shoot)

meteorite(float(input()), int(input()), float(input()))

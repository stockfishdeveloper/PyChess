import Position
def RMagic(piece, occupancy):
    topedge = 18374686479671623680
    rightedge = 9259542123273814144
    bottomedge = 255
    leftedge = 72340172838076673
    result = [0]
    current = [Position.GeneralBoard[piece]]
    if not Position.GeneralBoard[piece] & topedge:
        while True:
            current[0] <<= 8
            result[0] |= current[0]
            if (current[0] & topedge) or (current[0] & occupancy):
                break
    current[0] = Position.GeneralBoard[piece]
    if not Position.GeneralBoard[piece] & rightedge:
        while True:
            current[0] <<= 1
            result[0] |= current[0]
            if (current[0] & rightedge) or (current[0] & occupancy):
                break
    current[0] = Position.GeneralBoard[piece]
    if not Position.GeneralBoard[piece] & bottomedge:
        while True:
            current[0] >>= 8
            result[0] |= current[0]
            if (current[0] & bottomedge) or (current[0] & occupancy):
                break
    current[0] = Position.GeneralBoard[piece]
    if not Position.GeneralBoard[piece] & leftedge:
        while True:
            current[0] >>= 1
            result[0] |= current[0]
            if (current[0] & leftedge) or (current[0] & occupancy):
                break
    return result[0]

def BMagic(piece, occupancy):
    topedge = 18374686479671623680
    rightedge = 9259542123273814144
    bottomedge = 255
    leftedge = 72340172838076673
    result = [0]
    current = [Position.GeneralBoard[piece]]
    if not Position.GeneralBoard[piece] & (topedge | leftedge):
        while True:
            current[0] <<= 7
            result[0] |= current[0]
            if (current[0] & (topedge | leftedge)) or (current[0] & occupancy):
                break
    current[0] = Position.GeneralBoard[piece]
    if not Position.GeneralBoard[piece] & (rightedge | topedge):
        while True:
            current[0] <<= 9
            result[0] |= current[0]
            if (current[0] & (rightedge | topedge)) or (current[0] & occupancy):
                break
    current[0] = Position.GeneralBoard[piece]
    if not Position.GeneralBoard[piece] & (bottomedge | rightedge):
        while True:
            current[0] >>= 7
            result[0] |= current[0]
            if (current[0] & (bottomedge | rightedge)) or (current[0] & occupancy):
                break
    current[0] = Position.GeneralBoard[piece]
    if not Position.GeneralBoard[piece] & (leftedge | bottomedge):
        while True:
            current[0] >>= 9
            result[0] |= current[0]
            if (current[0] & (leftedge | bottomedge)) or (current[0] & occupancy):
                break
    return result[0]

def QMagic(piece, occupancy):
    return (RMagic(piece, occupancy) | BMagic(piece, occupancy))
    
    

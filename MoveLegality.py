import Position
def Is_Mate(position):
    score = [0]
    h = [0]
    for j in range(64):
        if position.White_King & Position.GeneralBoard[j]:
            h = j
            break
    BAttacks = 0#Bmagic(h, (position.White_Pieces | position.Black_Pieces))
    RAttacks = 0#Rmagic(h, (position.White_Pieces | position.Black_Pieces))
    QAttacks = 0#Qmagic(h, (position.White_Pieces | position.Black_Pieces))
    if BAttacks & position.Black_Bishops:
        score = -1
    if RAttacks & position.Black_Rooks:
        score = -1
    if QAttacks & position.Black_Queens:
        score = -1
    if Position.Knight_Lookup_Table[h] & position.Black_Knights:
        score = -1
    if Position.King_Lookup_Table[h] & position.Black_King:
        score = -1
    Spare = position.Black_Pawns
    Spare |= Position.A_Pawn_Mask
    Spare ^= Position.A_Pawn_Mask
    if Spare >> 7 & position.White_King:
        score = -1
    Spare2 = position.Black_Pawns
    Spare2 |= Position.H_Pawn_Mask
    Spare2 ^= Position.H_Pawn_Mask
    if Spare2 >> 9 & position.White_King:
        score = -1
    Black_Pawns5 = position.Black_Pawns
    Black_Pawns5 |= Position.A_Pawn_Mask
    Black_Pawns5 ^= Position.A_Pawn_Mask
    Black_Pawns5 |= Position.H_Pawn_Mask
    Black_Pawns5 ^= Position.H_Pawn_Mask
    if(((Black_Pawns5 >> 7) | (Black_Pawns5 >> 9)) & position.White_King):
        score = -1
    if(score != 0):
        if(score < 0):
            if(position.Current_Turn == True):
                return -10000
            else:
                return 10000
    for j in range(64):
        if(position.Black_King & Position.GeneralBoard[j]):
            h = j
            break
    BAttacks = 0#Bmagic(h, (position.White_Pieces | position.Black_Pieces))
    RAttacks = 0#Rmagic(h, (position.White_Pieces | position.Black_Pieces))
    QAttacks = 0#Qmagic(h, (position.White_Pieces | position.Black_Pieces))
    if BAttacks & position.White_Bishops:
        score = 1
    if RAttacks & position.White_Rooks:
        score = 1
    if QAttacks & position.White_Queens:
        score = 1
    if Position.Knight_Lookup_Table[h] & position.White_Knights:
        score = 1
    if Position.King_Lookup_Table[h] & position.White_King:
        score = 1
    Spare = position.White_Pawns
    Spare |= Position.A_Pawn_Mask;
    Spare ^= Position.A_Pawn_Mask;
    if((Spare << 9) & position.Black_King):
        score = 1
    Spare7 = position.White_Pawns
    Spare7 |= Position.H_Pawn_Mask
    Spare7 ^= Position.H_Pawn_Mask
    if((Spare7 << 7) & position.Black_King):
        score = 1
    White_Pawns2 = position.White_Pawns
    White_Pawns2 |= Position.A_Pawn_Mask
    White_Pawns2 ^= Position.A_Pawn_Mask
    White_Pawns2 |= Position.H_Pawn_Mask
    White_Pawns2 ^= Position.H_Pawn_Mask
    if(((White_Pawns2 << 7) | (White_Pawns2 << 9)) & Position.GeneralBoard[h]):
        score = 1
    if(score != 0):
        if(score > 0):
            if(position.Current_Turn == True):
                return 10000
            else:
                return -10000
    else:
        return 0

def White_Is_Legal(position, move):
    position.Make_Move(move);
    h = [0]
    for j in range(64):
        if position.White_King & Position.GeneralBoard[j]:
            h = j
            break
    BAttacks = 0#Bmagic(h, (position.White_Pieces | position.Black_Pieces))
    RAttacks = 0#Rmagic(h, (position.White_Pieces | position.Black_Pieces))
    QAttacks = BAttacks | RAttacks
    if QAttacks & position.Black_Queens:
        position.Undo_Move(move)
        return False
    if BAttacks & position.Black_Bishops:
        position.Undo_Move(move)
        return False
    if Position.Knight_Lookup_Table[h] & position.Black_Knights:
        position.Undo_Move(move)
        return False
    Spare = [position.Black_Pawns]
    Spare[0] |= Position.H_Pawn_Mask
    Spare[0] ^= Position.H_Pawn_Mask
    if((Spare[0] >> 7) & position.White_King):
        position.Undo_Move(move)
        return False
    Spare2 = [position.Black_Pawns]
    Spare2[0] |= Position.A_Pawn_Mask
    Spare2[0] ^= Position.A_Pawn_Mask
    if((Spare2[0] >> 9) & position.White_King):
        position.Undo_Move(move)
        return False
    if(RAttacks & (position.Black_Rooks)):
        position.Undo_Move(move)
        return False
    if(Position.King_Lookup_Table[h] & position.Black_King):
        position.Undo_Move(move)
        return False
    b = [position.Black_Pawns]
    b[0] |= Position.A_Pawn_Mask
    b[0] ^= Position.A_Pawn_Mask
    b[0] |= Position.H_Pawn_Mask
    b[0] ^= Position.H_Pawn_Mask
    if(((b[0] >> 7) | (b[0] >> 9)) & position.White_King):
        position.Undo_Move(move)
        return False
    position.Undo_Move(move)
    return True

def Black_Is_Legal(position, move):
    position.Make_Move(move)
    h = [0]
    for j in range(64):
        if position.Black_King & Position.GeneralBoard[j]:
            h = j
            break
    BAttacks = 0#Bmagic(h, (position.White_Pieces | position.Black_Pieces))
    RAttacks = 0#Rmagic(h, (position.White_Pieces | position.Black_Pieces))
    QAttacks = BAttacks | RAttacks
    if QAttacks & position.White_Queens:
        position.Undo_Move(move)
        return False
    if BAttacks & position.White_Bishops:
        position.Undo_Move(move)
        return False
    if Position.Knight_Lookup_Table[h] & position.White_Knights:
        position.Undo_Move(move)
        return False
    Spare2 = [position.White_Pawns]
    Spare2[0] |= Position.A_Pawn_Mask
    Spare2[0] ^= Position.A_Pawn_Mask
    if((Spare2[0] << 7) & position.Black_King):
        position.Undo_Move(move)
        return False
    Spare = [position.White_Pawns]
    Spare[0] |= Position.H_Pawn_Mask
    Spare[0] ^= Position.H_Pawn_Mask
    if((Spare[0] << 9) & position.Black_King):
        position.Undo_Move(move)
        return False
    if(RAttacks & (position.White_Rooks)):
        position.Undo_Move(move)
        return False
    if(Position.King_Lookup_Table[h] & position.White_King):
        position.Undo_Move(move)
        return False
    w = [position.White_Pawns]
    w[0] |= Position.A_Pawn_Mask
    w[0] ^= Position.A_Pawn_Mask
    w[0] |= Position.H_Pawn_Mask
    w[0] ^= Position.H_Pawn_Mask
    if(((w[0] << 7) | (w[0] << 9)) & position.Black_King):
        position.Undo_Move(move)
        return False
    else:
        position.Undo_Move(move)
        return True

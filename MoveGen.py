import Position
import MoveLegality
import Util
   
def Generate_White_Moves(position, caps):
    for i in range(64):
        if (position.White_Pawns & Position.GeneralBoard[i]) and (caps == False):
            if not((Position.GeneralBoard[i] << 8) & (position.White_Pieces | position.Black_Pieces)):
                m = Position.Move(Position.WP, Position.NONE, Position.GeneralBoard[i], Position.GeneralBoard[i] << 8, False, False)
                if MoveLegality.White_Is_Legal(position, m) == True:
                    position.LegalMoves.append(m)
            if (Position.GeneralBoard[i] & 65280) and not((position.White_Pawns << 16) & (position.White_Pieces | position.Black_Pieces)):
                m = Position.Move(Position.WP, Position.NONE, Position.GeneralBoard[i], Position.GeneralBoard[i] << 16, False, False)
                if MoveLegality.White_Is_Legal(position, m) == True:
                    position.LegalMoves.append(m)
            if not Position.GeneralBoard[i] & Position.A_Pawn_Mask:
                if(Position.GeneralBoard[i] << 7) & position.Black_Pieces:
                    m = Position.Move(Position.WP, position.Get_Piece_From_Bitboard(Position.GeneralBoard[i] << 7), Position.GeneralBoard[i], Position.GeneralBoard[i] << 7, False, False)
                    if MoveLegality.White_Is_Legal(position, m) == True:
                        position.LegalMoves.append(m)
            if not Position.GeneralBoard[i] & Position.H_Pawn_Mask:
                if(Position.GeneralBoard[i] << 9) & position.Black_Pieces:
                    m = Position.Move(Position.WP, position.Get_Piece_From_Bitboard(Position.GeneralBoard[i] << 9), Position.GeneralBoard[i], Position.GeneralBoard[i] << 9, False, False)
                    if MoveLegality.White_Is_Legal(position, m) == True:
                        position.LegalMoves.append(m)
            continue
        if position.White_Knights & Position.GeneralBoard[i]:
            b = [Position.Knight_Lookup_Table[i]]
            b[0] |= position.White_Pieces
            b[0] ^= position.White_Pieces
            p = Util.popcount(b[0])
            for m in range(p):
                j = Util.lsb(b[0])
                b[0] ^= Position.GeneralBoard[j]
                if Position.GeneralBoard[j] & position.Black_Pieces:
                    m = Position.Move(Position.WN, position.Get_Piece_From_Bitboard(Position.GeneralBoard[j]), Position.GeneralBoard[i], Position.GeneralBoard[j], False, False)
                    if MoveLegality.White_Is_Legal(position, m) == True:
                        position.LegalMoves.append(m)
                else:
                    if caps == False:
                        m = Position.Move(Position.WN, Position.NONE, Position.GeneralBoard[i], Position.GeneralBoard[j], False, False)
                        if(MoveLegality.White_Is_Legal(position, m)):
                            position.LegalMoves.append(m)
        if position.GeneralBoard[i] & position.White_Bishops):
	    b = [MagicMoves.Bmagic(i, position.White_Pieces | position.Black_Pieces)]
	    b[0] |= position.White_Pieces
	    b[0] ^= position.White_Pieces
	    p = Util.popcount(b)
	    for m in range(p):
		j = Util.lsb(b)
		b[0] ^= Position.GeneralBoard[j]
		if Position.GeneralBoard[j] & position.Black_Pieces:
		    m = Position.Move(Position.WB, position.Get_Piece_From_Bitboard(Position.GeneralBoard[j]), Position.GeneralBoard[i], Position.GeneralBoard[j], False, False)
		    if(MoveLegality.White_Is_Legal(position, m)) == True:
			position.LegalMoves.append(m)
						}
						else
							position.LegalMoves[position.numlegalmoves++] = m;
					}
				else
				{
					if(!caps)
					{
						Move m(WB, NONE, GeneralBoard[i], GeneralBoard[j], false, false);
						if(inCheck || (m.From & blockers))
						{
							if(White_Is_Legal(position, m))
								position.LegalMoves[position.numlegalmoves++] = m;
						}
						else
							position.LegalMoves[position.numlegalmoves++] = m;
					}
				}	
			}
		continue;
		}
    #for j in range(position.LegalMoves.__len__()):
        #position.LegalMoves[j].print()

        
def Generate_Black_Moves(position, caps):
    for i in range(64):
        if (position.Black_Pawns & Position.GeneralBoard[i]) and (caps == False):
            if not((Position.GeneralBoard[i] >> 8) & (position.White_Pieces | position.Black_Pieces)):
                m = Position.Move(Position.BP, Position.NONE, Position.GeneralBoard[i], Position.GeneralBoard[i] >> 8, False, False)
                if MoveLegality.Black_Is_Legal(position, m) == True:
                    position.LegalMoves.append(m)
            if (Position.GeneralBoard[i] & 71776119061217280) and not((position.White_Pawns >> 16) & (position.White_Pieces | position.Black_Pieces)):
                m = Position.Move(Position.BP, Position.NONE, Position.GeneralBoard[i], Position.GeneralBoard[i] >> 16, False, False)
                if MoveLegality.Black_Is_Legal(position, m) == True:
                    position.LegalMoves.append(m)
            if not Position.GeneralBoard[i] & Position.A_Pawn_Mask:
                if(Position.GeneralBoard[i] >> 9) & position.Black_Pieces:
                    m = Position.Move(Position.BP, position.Get_Piece_From_Bitboard(Position.GeneralBoard[i] >> 9), Position.GeneralBoard[i], Position.GeneralBoard[i] >> 9, False, False)
                    if MoveLegality.Black_Is_Legal(position, m) == True:
                        position.LegalMoves.append(m)
            if not Position.GeneralBoard[i] & Position.H_Pawn_Mask:
                if(Position.GeneralBoard[i] >> 7) & position.Black_Pieces:
                    m = Position.Move(Position.BP, position.Get_Piece_From_Bitboard(Position.GeneralBoard[i] >> 7), Position.GeneralBoard[i], Position.GeneralBoard[i] >> 7, False, False)
                    if MoveLegality.Black_Is_Legal(position, m) == True:
                        position.LegalMoves.append(m)
            continue
        if position.Black_Knights & Position.GeneralBoard[i]:
            b = [Position.Knight_Lookup_Table[i]]
            b[0] |= position.Black_Pieces
            b[0] ^= position.Black_Pieces
            p = Util.popcount(b[0])
            for m in range(p):
                j = Util.lsb(b[0])
                b[0] ^= Position.GeneralBoard[j]
                if Position.GeneralBoard[j] & position.White_Pieces:
                    m = Position.Move(Position.BN, position.Get_Piece_From_Bitboard(Position.GeneralBoard[j]), Position.GeneralBoard[i], Position.GeneralBoard[j], False, False);
                    if MoveLegality.Black_Is_Legal(position, m) == True:
                        position.LegalMoves.append(m)
                else:
                    if caps == False:
                        m = Position.Move(Position.BN, Position.NONE, Position.GeneralBoard[i], Position.GeneralBoard[j], False, False)
                        if(MoveLegality.Black_Is_Legal(position, m)):
                            position.LegalMoves.append(m)
    #for j in range(position.LegalMoves.__len__()):
        #position.LegalMoves[j].print()

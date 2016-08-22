import Position
import MoveGen
def Root_Perft(depth):
    if(depth == 0): return 0
    nodes = [0]
    if Position.pos.Current_Turn == True:
        MoveGen.Generate_White_Moves(Position.pos, False)
    else:
        MoveGen.Generate_Black_Moves(Position.pos, False)
    for i in range(Position.pos.LegalMoves.__len__()):
        Position.pos.Make_Move(Position.pos.LegalMoves[i])
        a = [""]
        for h in range(64):
            if Position.GeneralBoard[h] & Position.pos.LegalMoves[i].From:
                a[0] = Position.PlayerMoves[h]
        for h in range(64):
            if Position.GeneralBoard[h] & Position.pos.LegalMoves[i].To:
                a[0] += Position.PlayerMoves[h]
                if Position.pos.LegalMoves[i].Promotion == True:
                    if(Position.pos.LegalMoves[i].PromotionType == WN) or (Position.pos.LegalMoves[i].PromotionType == BN):
                        print("n")
                        break
                    if(Position.pos.LegalMoves[i].PromotionType == WB) or (Position.pos.LegalMoves[i].PromotionType == BB):
                        print("b")
                        break
                    if(Position.pos.LegalMoves[i].PromotionType == WR) or (Position.pos.LegalMoves[i].PromotionType == BR):
                        print("r")
                        break
                    if(Position.pos.LegalMoves[i].PromotionType == WQ) or (Position.pos.LegalMoves[i].PromotionType == BQ):
                        print("q")
                        break
                a[0] += ": "
        f = nodes[0]
        nodes[0] += Perft(Position.pos, depth - 1)
        print(a[0] + str(nodes[0] - f))
        Position.pos.Undo_Move(Position.pos.LegalMoves[i])
    return nodes[0]

def Perft(posit, depth):
    if depth == 0: return 1
    if depth == 1:
        position = Position.Position(posit)
        if position.Current_Turn == True:
            MoveGen.Generate_White_Moves(position, False)
        else:
            MoveGen.Generate_Black_Moves(position, False)
        return position.LegalMoves.__len__()
    position = Position.Position(posit)
    nodes = [0]
    if position.Current_Turn == True:
        MoveGen.Generate_White_Moves(position, False)
    else:
        MoveGen.Generate_Black_Moves(position, False)
    for i in range(position.LegalMoves.__len__()):
        position.Make_Move(position.LegalMoves[i])
        nodes[0] += Perft(position, depth - 1)
        position.Undo_Move(position.LegalMoves[i])
    return nodes[0]

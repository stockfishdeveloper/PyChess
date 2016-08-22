GeneralBoard = [] 
GeneralBoard = [
    1, 2, 4, 8, 16, 32, 64, 128,
    256, 512, 1024, 2048, 4096, 8192, 16384, 32768,
    65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608,
    16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648,
    4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888,
    1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416, 35184372088832, 70368744177664, 140737488355328,
    281474976710656, 562949953421312, 1125899906842624, 2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968,
    72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488, 1152921504606846976, 2305843009213693952, 4611686018427387904, 9223372036854775808
]
PlayerMoves = []
PlayerMoves = [

    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",

    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",

    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",

    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",

    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",

    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",

    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",

    "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"

]

Knight_Lookup_Table = []
Knight_Lookup_Table = [
    132096, 329728, 659712, 1319424, 2638848, 5277696, 10489856, 4202496,
    33816580, 84410376, 168886289, 337772578, 675545156, 1351090312, 2685403152, 1075839008,
    8657044482, 21609056261, 43234889994, 86469779988, 172939559976, 345879119952, 687463207072, 275414786112,
    2216203387392, 5531918402816, 11068131838464, 22136263676928, 44272527353856, 88545054707712, 175990581010432, 70506185244672,
    567348067172352, 1416171111120896, 2833441750646784, 5666883501293568, 11333767002587136, 22667534005174272, 45053588738670592, 18049583422636032,
    145241105196122112, 362539804446949376, 725361088165576704, 1450722176331153408, 2901444352662306816, 5802888705324613632, 11533718717099671552, 4620693356194824192,
    288234782788157440, 576469569871282176, 1224997833292120064, 2449995666584240128, 4899991333168480256, 9799982666336960512, 1152939783987658752, 2305878468463689728,
    1128098930098176, 2257297371824128, 4796069720358912, 9592139440717824, 19184278881435648, 38368557762871296, 4679521487814656, 9077567998918656
]
King_Lookup_Table = [
    770, 1797, 3594, 7188, 14376, 28752, 57504, 49216,
    197123, 460039, 920078, 1840156, 3680312, 7360624, 14721248, 12599488,
    50463488, 117769984, 235539968, 471079936, 942159872, 1884319744, 3768639488, 3225468928,
    12918652928, 30149115904, 60298231808, 120596463616, 241192927232, 482385854464, 964771708928, 825720045568,
    3307175149568, 7718173671424, 15436347342848, 30872694685696, 61745389371392, 123490778742784, 246981557485568, 211384331665408,
    846636838289408, 1975852459884544, 3951704919769088, 7903409839538176, 15806819679076352, 31613639358152704, 63227278716305408, 54114388906344448,
    216739030602088448, 505818229730443264, 1011636459460886528, 2023272918921773056, 4046545837843546112, 8093091675687092224, 16186183351374184448, 13853283560024178688,
    144959613005987840, 362258295026614272, 724516590053228544, 1449033180106457088, 2898066360212914176, 5796132720425828352, 11592265440851656704, 4665729213955833856
]
H_Pawn_Mask = 9259542123273814144
A_Pawn_Mask = 72340172838076673
G_Pawn_Mask = 4629771061636907072
B_Pawn_Mask = 144680345676153346
F_Pawn_Mask = 2314885530818453536
C_Pawn_Mask = 289360691352306692
E_Pawn_Mask = 1157442765409226768
D_Pawn_Mask = 578721382704613384

WP = 0
WN = 1
WB = 2
WR = 3
WQ = 4
WK = 5
BP = 6
BN = 7
BB = 8
BR = 9
BQ = 10
BK = 11
NONE = 12

def Print_Board():
    for h in range(64):
        if Position.GeneralBoard[h] & White_King:
            print('White king is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & Black_King:
            print('Black king is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & White_Queens:
            print('White queen is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & Black_Queens:
            print('Black queen is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & White_Rooks:
            print('White rook is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & Black_Rooks:
            print('Black rook is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & White_Bishops:
            print('White Bishop is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & Black_Bishops:
            print('Black Bishop is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & White_Knights:
            print('White Knight is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & Black_Knights:
            print('Black Knight is on ' +  PlayerMoves[h])
        if Position.GeneralBoard[h] & White_Pawns:
            print('White Pawn is on ' + PlayerMoves[h])
        if Position.GeneralBoard[h] & Black_Pawns:
            print('Black Pawn is on ' + PlayerMoves[h])
        
class Position:
    def __init__(self, position=None):
        self.White_Pieces = [0]
        self.Black_Pieces = [0]
        self.White_King = [0]
        self.Black_King = [0]
        self.White_Queens = [0]
        self.White_Rooks = [0]
        self.White_Bishops = [0]
        self.White_Knights = [0]
        self.White_Pawns = [0]
        self.Black_Queens = [0]
        self.Black_Rooks = [0]
        self.Black_Bishops = [0]
        self.Black_Knights = [0]
        self.Black_Pawns = [0]
        self.numlegalmoves = [0]
        self.WhiteCanCastleK = [False]
        self.WhiteCanCastleQ = [False]
        self.BlackCanCastleK = [False]
        self.BlackCanCastleQ = [False]
        self.Current_Turn = [True]
        self.hashkey = [0]
        self.numlegalmoves = [0]
        self.LegalMoves = []
        if position != None:
            self.Copy_Construct(position)
    def Copy_Construct(self, position):
        self.Current_Turn = position.Current_Turn
        self.White_Pieces = position.White_Pieces
        self.Black_Pieces = position.Black_Pieces
        self.White_King = position.White_King
        self.Black_King = position.Black_King
        self.White_Queens = position.White_Queens
        self.White_Rooks = position.White_Rooks
        self.White_Bishops = position.White_Bishops
        self.White_Knights = position.White_Knights
        self.White_Pawns = position.White_Pawns
        self.Black_Queens = position.Black_Queens
        self.Black_Rooks = position.Black_Rooks
        self.Black_Bishops = position.Black_Bishops
        self.Black_Knights = position.Black_Knights
        self.Black_Pawns = position.Black_Pawns
        self.WhiteCanCastleK = position.WhiteCanCastleK
        self.WhiteCanCastleQ = position.WhiteCanCastleQ
        self.BlackCanCastleK = position.BlackCanCastleK
        self.BlackCanCastleQ = position.BlackCanCastleQ
        self.hashkey = position.hashkey
        self.numlegalmoves = 0
    def Reset(self):
        self.White_Pieces = 65535
        self.Black_Pieces = 18446462598732840960
        self.White_King = 16
        self.Black_King = 1152921504606846976
        self.White_Queens = 8
        self.White_Rooks = 129
        self.White_Bishops = 36
        self.White_Knights = 66
        self.White_Pawns = 65280
        self.Black_Queens = 576460752303423488
        self.Black_Rooks = 9295429630892703744
        self.Black_Bishops = 2594073385365405696
        self.Black_Knights = 4755801206503243776
        self.Black_Pawns = 71776119061217280
        self.WhiteCanCastleK = True
        self.WhiteCanCastleQ = True
        self.BlackCanCastleK = True
        self.BlackCanCastleQ = True
        self.Current_Turn = True
        self.numlegalmoves = 0
        self.hashkey = 18446462598732906494
    def Get_Piece_From_Bitboard(self, b):
        if(b & self.White_Pawns):
            return WP
        if(b & self.White_Knights):
            return WN
        if(b & self.White_Bishops):
            return WB
        if(b & self.White_Rooks):
            return WR
        if(b & self.White_Queens):
            return WQ
        if(b & self.White_King):
            return WK
        if(b & self.Black_Pawns):
            return BP
        if(b & self.Black_Knights):
            return BN
        if(b & self.Black_Bishops):
            return BB
        if(b & self.Black_Rooks):
            return BR
        if(b & self.Black_Queens):
            return BQ
        if(b & self.Black_King):
            return BK
        return NONE
    def Make_Move(self, m):
        if m.Castling == True:
            if m.To & 64:
                self.White_Rooks |= 32
                self.White_Rooks ^= 128
                self.White_King |= 64
                self.White_King ^= 16
                self.White_Pieces ^= 144
                self.White_Pieces |= 96
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
            if m.To & 4611686018427387904:
                self.Black_Rooks |= 2305843009213693952
                self.Black_Rooks ^= 9223372036854775808
                self.Black_King |= 4611686018427387904
                self.Black_King ^= 1152921504606846976
                self.Black_Pieces ^= 10376293541461622784
                self.Black_Pieces |= 6917529027641081856
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
            if m.To & 4:
                self.White_Rooks |= 8
                self.White_Rooks ^= 1
                self.White_King |= 4
                self.White_King ^= 16
                self.White_Pieces ^= 17
                self.White_Pieces |= 12
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
            if m.To & 288230376151711744:
                self.Black_Rooks |= 576460752303423488
                self.Black_Rooks ^= 72057594037927936
                self.Black_King |= 288230376151711744
                self.Black_King ^= 1152921504606846976
                self.Black_Pieces ^= 1224979098644774912
                self.Black_Pieces |= 864691128455135232
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
        if m.P == WP:
            self.White_Pawns ^= m.From
            self.White_Pawns |= m.To
        if m.P == WN:
            self.White_Knights ^= m.From
            self.White_Knights |= m.To
        if m.P == WB:
            self.White_Bishops ^= m.From
            self.White_Bishops |= m.To
        if m.P == WR:
            self.White_Rooks ^= m.From
            self.White_Rooks |= m.To
        if m.P == WQ:
            self.White_Queens ^= m.From
            self.White_Queens |= m.To
        if m.P == WK:
            self.White_King ^= m.From
            self.White_King |= m.To
        if m.P == BP:
            self.Black_Pawns ^= m.From
            self.Black_Pawns |= m.To
        if m.P == BN:
            self.Black_Knights ^= m.From
            self.Black_Knights |= m.To
        if m.P == BB:
            self.Black_Bishops ^= m.From
            self.Black_Bishops |= m.To
        if m.P == BR:
            self.Black_Rooks ^= m.From
            self.Black_Rooks |= m.To
        if m.P == BQ:
            self.Black_Queens ^= m.From
            self.Black_Queens |= m.To
        if m.P == BK:
            self.Black_King ^= m.From
            self.Black_King |= m.To
        if m.P > WK:
            self.Black_Pieces |= m.To
            self.Black_Pieces ^= m.From
        else:
            self.White_Pieces |= m.To
            self.White_Pieces ^= m.From
        if(m.C != NONE):
            if m.C == WP:
                self.White_Pawns ^= m.To
            if m.C == WN:
                self.White_Knights ^= m.To
            if m.C == WB:
                self.White_Bishops ^= m.To
            if m.C == WR:
                self.White_Rooks ^= m.To
            if m.C == WQ:
                self.White_Queens ^= m.To
            if m.C == BP:
                self.Black_Pawns ^= m.To
            if m.C == BN:
                self.Black_Knights ^= m.To
            if m.C == BB:
                self.Black_Bishops ^= m.To
            if m.C == BR:
                self.Black_Rooks ^= m.To
            if m.C == BQ:
                self.Black_Queens ^= m.To
            if m.C > WK:
                self.Black_Pieces ^= m.To
            else:
                self.White_Pieces ^= m.To
        if m.Promotion == True:
            if m.PromotionType == WN:
                self.White_Knights |= m.To
            if m.PromotionType == WB:
                self.White_Bishops |= m.To
            if m.PromotionType == WR:
                self.White_Rooks |= m.To
            if m.PromotionType == WQ:
                self.White_Queens |= m.To
            if m.PromotionType == BN:
                self.Black_Knights |= m.To
            if m.PromotionType == BB:
                self.Black_Bishops |= m.To
            if m.PromotionType == BR:
                self.Black_Rooks |= m.To
            if m.PromotionType == BQ:
                self.Black_Queens |= m.To
            if self.Current_Turn == True:
                self.White_Pawns ^= m.To
            else:
                self.Black_pawns ^= m.To
        if self.Current_Turn == True:
            self.Current_Turn = False
        else:
            self.Current_Turn = True
        return
    def Undo_Move(self, m):
        if m.Castling == True:
            if m.To & 64:
                White_Rooks ^= 32
                White_Rooks |= 128
                White_King ^= 64
                White_King |= 16
                White_Pieces |= 144
                White_Pieces ^= 96
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
            if(m.To & 4611686018427387904):
                Black_Rooks ^= 2305843009213693952
                Black_Rooks |= 9223372036854775808
                Black_King ^= 4611686018427387904
                Black_King |= 1152921504606846976
                Black_Pieces |= 10376293541461622784
                Black_Pieces ^= 6917529027641081856
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
            if m.To & 4:
                White_Rooks ^= 8
                White_Rooks |= 1
                White_King ^= 4
                White_King |= 16
                White_Pieces |= 17
                White_Pieces ^= 12
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
            if m.To & 288230376151711744:
                Black_Rooks ^= 576460752303423488
                Black_Rooks |= 72057594037927936
                Black_King ^= 288230376151711744
                Black_King |= 1152921504606846976
                Black_Pieces |= 1224979098644774912
                Black_Pieces ^= 864691128455135232
                if self.Current_Turn == True:
                    self.Current_Turn = False
                else:
                    self.Current_Turn = True
                return
        if m.P == WP:
            self.White_Pawns |= m.From
            self.White_Pawns ^= m.To
        if m.P == WN:
            self.White_Knights |= m.From
            self.White_Knights ^= m.To
        if m.P == WB:
            self.White_Bishops |= m.From
            self.White_Bishops ^= m.To
        if m.P == WR:
            self.White_Rooks |= m.From
            self.White_Rooks ^= m.To
        if m.P == WQ:
            self.White_Queens |= m.From
            self.White_Queens ^= m.To
        if m.P == WK:
            self.White_King |= m.From
            self.White_King ^= m.To
        if m.P == BP:
            self.Black_Pawns |= m.From
            self.Black_Pawns ^= m.To
        if m.P == BN:
            self.Black_Knights |= m.From
            self.Black_Knights ^= m.To
        if m.P == BB:
            self.Black_Bishops |= m.From
            self.Black_Bishops ^= m.To
        if m.P == BR:
            self.Black_Rooks |= m.From
            self.Black_Rooks ^= m.To
        if m.P == BQ:
            self.Black_Queens |= m.From
            self.Black_Queens ^= m.To
        if m.P == BK:
            self.Black_King |= m.From
            self.Black_King ^= m.To
        if m.P > WK:
            self.Black_Pieces ^= m.To
            self.Black_Pieces |= m.From
        else:
            self.White_Pieces ^= m.To
            self.White_Pieces |= m.From
        if(m.C != NONE):
            if m.C == WP:
                self.White_Pawns |= m.To
            if m.C == WN:
                self.White_Knights |= m.To
            if m.C == WB:
                self.White_Bishops |= m.To
            if m.C == WR:
                self.White_Rooks |= m.To
            if m.C == WQ:
                self.White_Queens |= m.To
            if m.C == BP:
                self.Black_Pawns |= m.To
            if m.C == BN:
                self.Black_Knights |= m.To
            if m.C == BB:
                self.Black_Bishops |= m.To
            if m.C == BR:
                self.Black_Rooks |= m.To
            if m.C == BQ:
                self.Black_Queens |= m.To
            if m.C > WK:
                self.Black_Pieces |= m.To
            else:
                self.White_Pieces |= m.To
        if(m.Promotion == True):
            if m.PromotionType == WN:
                self.White_Knights ^= m.To
            if m.PromotionType == WB:
                self.White_Bishops ^= m.To
            if m.PromotionType == WR:
                self.White_Rooks ^= m.To
            if m.PromotionType == WQ:
                self.White_Queens ^= m.To
            if m.PromotionType == BN:
                self.Black_Knights ^= m.To
            if m.PromotionType == BB:
                self.Black_Bishops ^= m.To
            if m.PromotionType == BR:
                self.Black_Rooks ^= m.To
            if m.PromotionType == BQ:
                self.Black_Queens ^= m.To
            if self.Current_Turn == True:
                self.White_Pawns ^= m.To
            else:
                self.Black_pawns ^= m.To
        if self.Current_Turn == True:
            self.Current_Turn = False
        else:
            self.Current_Turn = True
class Move:
    def __init__(self, piece, captured, from1, to, castling, promotion):
        self.P = piece
        self.C = captured
        self.From = from1
        self.To = to
        self.Score = castling
        self.Castling = castling
        self.Promotion = promotion
        self.PromotionType = NONE
    def print(self):
        s = ""
        for i in range(64):
            if self.From == GeneralBoard[i]:
                s += PlayerMoves[i]
        for i in range(64):
            if self.To == GeneralBoard[i]:
                s += PlayerMoves[i]
        print(s)
pos = Position()
   

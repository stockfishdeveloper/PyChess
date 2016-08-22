import Position
import MoveGen
import Perft
import time
def Uci_Loop():
    while True:
        UciCommand = input()
        if UciCommand == 'uci':
            print('id name Chess\nid author David Cimbalista\n' +  
              'option name TimePerMove type spin default 3 min 1 max 5\n' +
              'uciok\n')
        if UciCommand == 'isready':
            print('readyok\n')
        if UciCommand == 'startpos':
            p = Position.Position()
            p.Reset()
            Position.pos = p
        if UciCommand == "perft":
            t = int(round(time.time() * 1000.0))
            depth = [0]
            depth[0] = input()
            nodes = Perft.Root_Perft(int(depth[0]));
            print("\n===========================\n")
            t1 = (int(round(time.time() * 1000.0)) - t)
            print("Total time (ms) : " + str(t1) + "\n")
            print("Nodes searched  : " + str(nodes) + "\n")
            print("Nodes/second    : " + str(int(round((nodes / (t1 + 1) * 1000)))) + "\n")
            
                

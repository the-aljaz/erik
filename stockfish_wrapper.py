import socket
from stockfish import Stockfish


#! ENGINE INITIALIZATION
STOCKFISH_PATH = "stockfish\stockfish-windows-x86-64-avx2.exe" #MORE BIT RELATIVEN !!!!!!!!!!!!!!!!!!!!

stockfish = Stockfish(path=STOCKFISH_PATH, depth=18, parameters={"Threads": 7, "Minimum Thinking Time": 8}) # 18 is the depth of the engine
stockfish.update_engine_parameters({"Hash": 2048})


fm = stockfish.get_best_move()


moves =  [fm]
for i in range(5):
    stockfish.set_position(moves)
    moves.append(stockfish.get_best_move())
print(stockfish.get_board_visual())

print(moves)
import re
import sys 
import chess
import chess.uci
from stockfish import Stockfish
import chess.pgn
from pprint import pprint


# Here you need to add the path to stockfish or some other uci engine(that will probably work)
engine = Stockfish("/usr/bin/stockfish")
san_regex = re.compile('([KQNBR]([a-h][1-8])?x)?[KQNBR]?[a-h][1-8]$|[0o]-[o0]$')
uci_regex = re.compile('[a-h][1-8][a-h][1-8]')

moves = []
emoves = []
board = chess.Board()

game_commands=['fen','help','undo','dif','help','board','params','exit']

def execute_command(command):
        print('executing the command')
        if command == 'fen':
                print(engine.gen_fen_position())
        elif command == 'help':
                print('Welcome to Blind Chess, you can enter moves both in SAN form(e4, Kf6 etc.) or UCI (e2e4,e7e5).\n'+
                        'Extra commands:\n'+
                        '1. fen:   returns a FEN representation of the board\n' +
                        '2. undo:  unmakes last move\n' +
                        '3. dif:   difficulty level(1-20)\n' +
                        '4. help:  returns this menu\n' +
                        '5. board: see the board\n' +
                        '6. params: Display engine parameters\n'+
                        '7. exit:  exit Blind Chess')

        elif command == 'undo':
            if len(moves) > 1:
                del moves[-1]
                del moves[-1]
                print("Undid last move.")
                engine.set_position(moves)
            else:
                print("No moves to undo.")

        elif command == 'board':
                print(engine.get_board_visual())

        elif command == 'dif':
                dif = input("Enter game difficulty(1-20):")
                engine.set_skill_level(int(dif))

        elif command == 'params':
                print(engine.get_parameters())

        elif command == 'exit':
                sys.exit("Goodbye!")

def move_to_san(move,stockfish,board):

    fen = stockfish.get_fen_position()
    board.set_fen(fen)
    move = board.parse_san(move)
    
    return board.san(move), move


while True:
        players_move = input("Please enter your move:")

        if players_move in game_commands:
                execute_command(players_move)
                continue

        else:
                if True:
                    mymove, emove = move_to_san(players_move, engine, board)
                    moves.append(mymove)
                    emoves.append(emove)

                    # Updates move
                    engine.set_position(emoves)

                    # Makes engine move
                    engine_move,emove = move_to_san(engine.get_best_move(), engine, board)

                    # Condition for game over
                    # get_best_move() returns false on mate
                    if engine_move == False:
                        print('Game over')
                        print(engine.get_board_visual())
                        sys.exit("Goodbye!")

                    # Updates move list
                    moves.append(engine_move)
                    emoves.append(emove)
                    engine.set_position(emoves)

                    # Print all moves after each round
                    index = 0
                    move_num = 0
                    for m in moves:

                            if (index % 2) == 0 :
                                    move_num = move_num + 1
                                    print(str(move_num)+'.'+ str(m), end='')
                            else :
                                    print(' ,'+str(m))

                            index = index + 1

                else:
                    print("Move or command not found, please try entering a valid move or command")



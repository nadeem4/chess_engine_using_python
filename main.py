import copy

import chess
import chess.engine
from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def fib(n):
    if n <= 1:
        return n
    return fib(n=n - 1) + fib(n=n - 2)


def static_eval(board_instance, depth):
    move = engine.analyse(board, chess.engine.Limit(time=0.01))
    return chess.engine.PovScore(move['score'], chess.WHITE).pov(chess.WHITE).relative.score()


def minmax(board_instance, depth, is_max_player):
    if depth == 0:
        return static_eval(board_instance, depth)

    if is_max_player:

        # set absurdly high negative value such that none of the static evaluation result less than this value
        max_val = -100000

        for move in board_instance.legal_moves:
            # here we are creating a shallow copy of board at every iteration to try all possible move on a current board instance
            copied_board_instance = copy.copy(board_instance)

            # pusshing the current move to the board
            copied_board_instance.push(move)
            node_val = minmax(copied_board_instance, depth - 1, False)
            max_val = max(node_val, max_val)
            copied_board_instance.pop()
        return max_val
    else:

        # set absurdly high positive value such that none of the static evaluation result more than this value
        min_val = 100000

        for move in board_instance.legal_moves:
            # here we are creating a shallow copy of board at every iteration to try all possible move on a current board instance
            copied_board_instance = copy.copy(board_instance)

            # pusshing the current move to the board
            copied_board_instance.push(move)
            node_val = minmax(copied_board_instance, depth - 1, True)
            min_val = min(node_val, min_val)
            copied_board_instance.pop()
        return min_val


if __name__ == '__main__':
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("stockfish_13_win_x64_bmi2/stockfish_13_win_x64_bmi2.exe")
    print(engine)
    print(board)

    print(fib(n=6))
    # Save recursion tree to a file
    vs.make_animation("fibonacci.gif", delay=2)

    engine.quit()

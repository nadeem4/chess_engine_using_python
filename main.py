import chess
import chess.engine
from memory_profiler import profile


def static_eval(board_instance):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board_instance.piece_at(i).color)
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        evaluation = evaluation + (
            get_piece_val(str(board_instance.piece_at(i))) if x else -get_piece_val(str(board_instance.piece_at(i))))
    return evaluation


def get_piece_val(piece):
    if piece is None:
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 10
    if piece == "N" or piece == "n":
        value = 30
    if piece == "B" or piece == "b":
        value = 30
    if piece == "R" or piece == "r":
        value = 50
    if piece == "Q" or piece == "q":
        value = 90
    if piece == 'K' or piece == 'k':
        value = 900
    # value = value if (board.piece_at(place)).color else -value
    return value


def minmax(board_instance, depth, is_max_player):
    # This is the base case
    if depth == 0:
        leaf_node_score = static_eval(board_instance)
        return leaf_node_score

    if is_max_player:

        # set absurdly high negative value such that none of the static evaluation result less than this value
        best_score = -100000

        for legal_move in board_instance.legal_moves:
            move = chess.Move.from_uci(str(legal_move))

            # pushing the current move to the board
            board_instance.push(move)

            # calculating the max value for the particular node
            best_score = max(best_score, minmax(board_instance, depth - 1, False))

            # undoing the last move, so that we can evaluate next legal moves
            board_instance.pop()

        return best_score
    else:

        # set absurdly high positive value such that none of the static evaluation result more than this value
        best_score = 100000

        for legal_move in board_instance.legal_moves:
            move = chess.Move.from_uci(str(legal_move))

            # pushing the current move to the board
            board_instance.push(move)

            # calculating the min value for the particular node
            best_score = min(best_score, minmax(board_instance, depth - 1, True))

            # undoing the last move, so that we can evaluate next legal moves
            board_instance.pop()
        return best_score


def best_move_using_minmax(board_instance, depth, is_max_player):
    best_move_score = -1000000
    best_move = None
    for legal_move in board_instance.legal_moves:
        move = chess.Move.from_uci(str(legal_move))
        board_instance.push(move)
        score = max(best_move_score, minmax(board_instance, depth, False))
        board_instance.pop()
        if score > best_move_score:
            best_move_score = score
            best_move = move
    return best_move


if __name__ == '__main__':
    board = chess.Board()
    print(board)

    move = best_move_using_minmax(board, 3, True)
    print(move)


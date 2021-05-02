  
import chess

p = 1

PawnBottomMatrix = [[3*p,3*p,3*p,4*p,4*p,3*p,3*p,3*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[0*p,1*p,1*p,1*p,1*p,1*p,1*p,0*p],[0*p,0*p,0*p,0*p,0*p,0*p,0*p,0*p]]

PawnTopMatrix = [[0*p,0*p,0*p,0*p,0*p,0*p,0*p,0*p],[0*p,1*p,1*p,1*p,1*p,1*p,1*p,0*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[3*p,3*p,3*p,4*p,4*p,3*p,3*p,3*p]]

RockButtomMatrix = [[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p]]

RockTopMatrix = [[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p]]

BishopButtomMatrix = [[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p]]

BishopTopMatrix = [[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p]]

KingButtomMatrix = [[-5*p,1*p,2*p,2*p,2*p,2*p,1*p,-5*p],[-1*p,2*p,2*p,2*p,2*p,2*p,2*p,-1*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[-1*p,2*p,2*p,2*p,2*p,2*p,2*p,-1*p],[-5*p,1*p,2*p,2*p,2*p,2*p,1*p,-5*p]]

KingTopMatrix = [[-5*p,1*p,2*p,2*p,2*p,2*p,1*p,-5*p],[-1*p,2*p,2*p,2*p,2*p,2*p,2*p,-1*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[0*p,2*p,2*p,2*p,2*p,2*p,2*p,0*p],[-1*p,2*p,2*p,2*p,2*p,2*p,2*p,-1*p],[-5*p,1*p,2*p,2*p,2*p,2*p,1*p,-5*p]]

QueenButtomMatrix = [[0*p,1*p,1*p,1*p,1*p,1*p,1*p,0*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[0*p,1*p,1*p,1*p,1*p,1*p,1*p,0*p]]

QueenTopMatrix = [[0*p,1*p,1*p,1*p,1*p,1*p,1*p,0*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1.5*p,2*p,2*p,2*p,2*p,2*p,2*p,1.5*p],[1*p,2*p,2*p,2*p,2*p,2*p,2*p,1*p],[0*p,1*p,1*p,1*p,1*p,1*p,1*p,0*p]]

KnightButtomMatrix = [[-2*p,-1*p,0*p,0*p,0*p,0*p,-1*p,-2*p],[-1*p,0*p,1*p,1*p,1*p,1*p,0*p,-1*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[-1*p,0*p,1*p,1*p,1*p,1*p,0*p,-1*p],[-2*p,-1*p,0*p,0*p,0*p,0*p,-1*p,-2*p]]

KnightTopMatrix = [[-2*p,-1*p,0*p,0*p,0*p,0*p,-1*p,-2*p],[-1*p,0*p,1*p,1*p,1*p,1*p,0*p,-1*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[0*p,1*p,2*p,2*p,2*p,2*p,1*p,0*p],[-1*p,0*p,1*p,1*p,1*p,1*p,0*p,-1*p],[-2*p,-1*p,0*p,0*p,0*p,0*p,-1*p,-2*p]]


def getaction(depth, board, is_max):
    possible_moves = board.legal_moves
    best_value = -float("inf")
    final_best_move = None
    for x in possible_moves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        value = max(best_value, minmax(depth - 1, board,-float("inf"),float("inf"), not is_max))
        board.pop()
        if( value > best_value):
            best_value = value
            final_best_move = move
    return final_best_move

def minmax(depth, board, alpha, beta, is_max):
    if(depth == 0):
        return -evaluation(board)
    possible_moves = board.legal_moves
    if(is_max):
        best_move = -float("inf")
        for x in possible_moves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            best_move = max(best_move,minmax(depth - 1, board,alpha,beta, not is_max))
            board.pop()
            alpha = max(alpha,best_move)
            # do the alpha beta pruning
            if beta <= alpha:
                return best_move
        return best_move
    else:
        best_move = float("inf")
        for x in possible_moves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            best_move = min(best_move, minmax(depth - 1, board,alpha,beta, not is_max))
            board.pop()
            beta = min(beta,best_move)
            # do the alpha beta pruning
            if(beta <= alpha):
                return best_move
        return best_move


def evaluation(board):
    i = 0
    evaluation = 0
    while i < 63:
        piece = board.piece_at(i)
        if piece:
            role = bool(board.piece_at(i).color)
            x, y = i//8, i%8
            evaluation += (getPieceValue(str(board.piece_at(i)),x,y) if role else -getPieceValue(str(board.piece_at(i)),x,y))
        i += 1
    return evaluation


def getPieceValue(piece, x, y):
    if(piece == None):
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 5 + PawnBottomMatrix[x][y]
    if piece == "N" or piece == "n":
        value = 10 + KingButtomMatrix[x][y]
    if piece == "B" or piece == "b":
        value = 20 + BishopButtomMatrix[x][y]
    if piece == "R" or piece == "r":
        value = 40 + RockButtomMatrix[x][y]
    if piece == "Q" or piece == "q":
        value = 100 + QueenButtomMatrix[x][y]
    if piece == 'K' or piece == 'k':
        value = 1000 + KingButtomMatrix[x][y]
    return value

def main():
    board = chess.Board()
    n = 0
    print(board)
    print(chess.Piece)
    while not board.is_game_over():
        if n%2 == 0:
            print(board.legal_moves)
            move = input("Please enter  a valid move or enter exit to quit: ")
            if move == "exit":
                break
            move = chess.Move.from_uci(str(move))
            board.push(move)
        else:
            print("AI move:")
            move = getaction(3, board, True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        print(board)
        n += 1
    print("Quit game successfully")
    print(board.outcome)
if __name__ == "__main__":
    main()

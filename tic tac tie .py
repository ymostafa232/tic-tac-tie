#a tic tac tie program
# i tried to make it so simple to  beginner to understand and for all programmers
X = 'X'
O = 'O'
TIE = 'TIE'
EMPTY = ' '
NUM_SQUARES = 9


def display_instructions ():
    """the instruction of the game"""
    print("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
This will be a showdown between your human brain and my silicon processor.
You will make your move known by entering a number, 0 - 8. The number
will correspond to the board position as illustrated:
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
     prepare your self man because i'm playing for all of my kind ^-^
                
""")


def ask_yes_no_que (question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def new_board():
    """displaying an empty board"""

    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)

    return board


def the_pieces():
    go_first = ask_yes_no_que("do you wanna go first ?? (y,n) : ")
    if go_first == 'y':
        print("then you first ")
        human = X
        computer = O
    else:
        print("you will regret for your bravery ")
        human = O
        computer = X
    return human, computer


def display_the_board(board):
    print('\t', board[0], ' ', '|', board[1], ' ', '|', board[2])
    print('\t', "-"*15)
    print('\t', board[3], ' ', '|', board[4], ' ', '|', board[5])
    print('\t', '-'*15)
    print('\t', board[6], ' ', '|', board[7], ' ', '|', board[8])


def legal_moves(board):
    move = []
    for i in range(NUM_SQUARES):
        if board[i] == EMPTY:
            move.append(i)
    return move


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board :
        return TIE
    return None


def the_human_move(board ):
    legal = legal_moves(board)
    response = None
    while response not in legal :
        response = int(input("enter your move :  "))
        if response not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    return response


def computer_move(board, human, computer):
    # make a copy to work with since function will be changing list
    board = board[:]
    BEST_MOVES = [4, 0, 2, 6, 8, 3, 5]
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer :
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_move(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_the_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, 'won')
    else:
        print("it's a tie")
    # the following statements are just for fun
    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more. \n" \
        "Proof that computers are superior to humans in all regards.")
    elif the_winner == human:
        print("No, no! It cannot be! Somehow you tricked me, human. \n" \
        "But never again! I, the computer, so swear it!")
    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n" \
        "Celebrate today... for this is the best you will ever achieve.")


display_instructions()
human , computer =the_pieces()
turn = X
board = new_board()
display_the_board(board)
while not winner(board):
        if turn == human:
            move = the_human_move(board)
            board[move] = human
        else:
            move = computer_move(board, human, computer)
            board[move] = computer

        display_the_board(board)
        turn = next_move(turn)

the_winner = winner(board)
congrat_the_winner(the_winner, computer, human)



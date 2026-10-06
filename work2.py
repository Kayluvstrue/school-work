board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

current_player = "X"


def update_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def get_valid_int():
    while True:
        try:
            spot = int(input("choose a spot 1 to 9: "))

            if 1 <= spot <= 9:
                return spot - 1
            else:
                print("choose a number from 1 to 9")

        except ValueError:
            print("enter a number.")


def player_turn():
    while True:
        spot = get_valid_int()

        if board[spot] == " ":
            board[spot] = current_player
            break
        else:
            print("the spot is taken")


def check_win():
    if board[0] == board[1] == board[2] and board[0] != " ":
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return True
    elif board[0] == board[3] == board[6] and board[0] != " ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        return True
    elif board[0] == board[4] == board[8] and board[0] != " ":
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        return True

    return False


def tie():
    if " " not in board:
        return True
    return False


def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def game():
    global current_player

    while True:
        update_board()

        print("player " + current_player + "s turn")
        player_turn()

        if check_win():
            update_board()
            print("player " + current_player + " wins")
            break

        if tie():
            update_board()
            print("its a tie")
            break

        switch_player()


game()
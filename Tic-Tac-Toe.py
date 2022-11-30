#!/bin/python3

def display_board(board):
    print("-----")
    print(board[0] + "|" + board[1] + "|" +board[2])
    print("1|2|3")
    print("-----")
    print(board[3] + "|" + board[4] + "|" +board[5])
    print("4|5|6")
    print("-----")
    print(board[6] + "|" + board[7] + "|" +board[8])
    print("7|8|9")
    print("-----")

def take_input(turn,board):
    pos = "0"
    pl = -1
    if turn%2 == 0:
        pl = 2
    else:
        pl = 1
    while int(pos) not in [1,2,3,4,5,6,7,8,9] or board[int(pos)-1] != " ":
        pos = input("Player {} Select your position : ".format(pl))
    return int(pos)

def is_gameon():
    on = "0"
    while on not in ["Y","N","y","n"]:
        on = input("Want to keep playing? (Y / N): ")
    if on =="Y" or on =="y":
        return True
    else:
        return False

def update_board(board,pos,mark):
    board[pos-1] = mark
    return board

def check_result(board):
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        return (True,"1")
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        return (True,"1")
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        return (True,"1")
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        return (True,"1")
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        return (True,"1")
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        return (True,"1")    
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        return (True,"1")
    if board[2] == "X" and board[4] == "X" and board[6] == "X":
        return (True,"1")    
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        return (True,"2")
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        return (True,"2")
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        return (True,"2")
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        return (True,"2")
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        return (True,"2")
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        return (True,"2")    
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        return (True,"2")
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        return (True,"2")  
    return (False,"N")

def init_board():
    return [" "," "," "," "," "," "," "," "," "]


#Main logic
gameon=True

while gameon:
    turn = 1
    board = init_board()
    display_board(board)
    while True and turn<=9:
        pos = take_input(turn,board)
        if turn%2 == 1:
            board = update_board(board,pos,"X")
        else:
            board = update_board(board,pos,"O")
        display_board(board)
        res = check_result(board)
        #print("Value {}. Type {}".format(res,type(res)))
        if res[0]:
            print("Player {} wins!!".format(res[1]))
            break
        turn += 1
    if turn > 9:
        print("Game Drawn :(")
    gameon = is_gameon()

import os, time, sys
from termcolor import colored

state = 1
#koordynaty sasiednich pol
NW = [-1, -1]
N = [-1, 0]
NE = [-1, 1]
E = [0, 1]
SE = [1, 1]
S = [1, 0]
SW = [1, -1]
W = [0, -1]
####
#def start():

def create_board(board_size, field):
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            if i==1:
                row.append("P1")
            elif i==6:
                row.append("P2")
            else:
                row.append(field)
        board.append(row)
    board[0][0], board[0][7], board[7][0], board[7][7] = "W1", "W1", "W2", "W2" #wieza
    board[0][1], board[0][6], board[7][1], board[7][6] = "S1", "S1", "S2", "S2" #skoczek
    board[0][2], board[0][5], board[7][2], board[7][5] = "G1", "G1", "G2", "G2" #goniec
    board[0][4], board[7][3] = "H1", "H2" #hetman
    board[0][3], board[7][4] = "K1", "K2" #krol
    return board

def show_board(board, board_size):
    for row in range(board_size + 2):
        line = ""
        for column in range(board_size + 2):
            line += "----"
    print line + "-"

    for row in range(board_size):
        line = " "
        line2 = ""
        for column in range(board_size):
            if str(board[row][column]).find('1') == -1:
                line += colored(str(board[row][column]), 'grey') + " | "
            else:
                line += colored(str(board[row][column]), 'white') + " | "
            line2 += "----"
        print "|" + line
        print line2 + "---------"

def move(board, board_size):
    show_board(board, board_size)
    while state:
        print "Ruch gracza:", player
        print("Wybierz figure:")
        # try:
        piece_row = int(raw_input("Podaj wiersz: > ")) - 1
        piece_column = int(raw_input("Podaj kolumne: > ")) - 1
        # except ValueError:
        #     print "To nie jest poprawna wartosc! Sprobuj jeszcze raz!"
        #     move(board, 8)
        # except KeyboardInterrupt:
        #     decision_state = 1
        #     while decision_state:
        #         decision = raw_input("Czy zakonczyc gre? (T/N)")
        #         print decision
        #         if decision == 'T':
        #             print "KONIEC GRY"
        #             decision_state == 0;
        #             sys.exit()
        #         elif decision == 'N':
        #             print "Powrot do gry!"
        #             move(board, 8)
        # try:
        chosen_piece = board[piece_row][piece_column]
        # except IndexError:
        #     print "Wprowadz cyfre od 1 do 8! Sprobuj jeszcze raz!"
        #     move(board, 8)
        if(chosen_piece == "  "):
            print("Puste pole! Wybierz inne!")
            time.sleep(2)
            move(board, 8)
        elif((chosen_piece.find('1') > -1 and player.find('1') > -1) or (chosen_piece.find('2') > -1 and player.find('2') > -1)):
            print "Wybrano figure:", chosen_piece
            print("Przesun na pole:")
            to_row = int(raw_input("Podaj wiersz: > ")) - 1
            to_column = int(raw_input("Podaj kolumne: > ")) - 1
            if board[to_row][to_column] == board[piece_row][piece_column]:
                print("Wybor anulowano. Powtorz akcje!")
                move(board, 8)
            else:
                if((str(board[to_row][to_column]).find('1') > -1 and player.find('1') > -1) or (str(board[to_row][to_column]).find('2') > -1 and player.find('2') > -1)):
                    print("Nie mozesz zbic swojej figury!")
                    time.sleep(2)
                    move(board, 8)
                elif(str(board[to_row][to_column]) == "  "):
                    print "Ruch na puste pole!"
                    board[to_row][to_column] = chosen_piece
                    board[piece_row][piece_column] = "  "
                    break
                else:
                    board[to_row][to_column] = chosen_piece
                    print "Zbito figure przeciwnika:", chosen_piece
                    board[piece_row][piece_column] = "  "
                    break
        else:
            print("Nie mozesz ruszac figury przeciwnika!")
            time.sleep(2)
            move(board, 8)

if __name__ == "__main__":
    board = create_board(8, "  ")
    while state:
        player = 'Gracz1(White)'
        move(board, 8)
        player = 'Gracz2(Black)'
        move(board, 8)
    if not state:
        print("Koniec gry!")
        print "Wygrana:", player

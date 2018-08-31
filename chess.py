import os, time
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
        piece_row = int(raw_input("Podaj wiersz: > ")) - 1
        piece_column = int(raw_input("Podaj kolumne: > ")) - 1
        chosen_piece = board[piece_row][piece_column]
        if(chosen_piece == "  "):
            print("Puste pole! Wybierz inne!")
            time.sleep(3)
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
                print "Gracz", player ,player.find('1')
                print "Ruszam na", str(board[to_row][to_column]), str(board[to_row][to_column]).find('1')
                if((str(board[to_row][to_column]).find('1') > -1 and player.find('1') > -1) or (str(board[to_row][to_column]).find('2') > -1 and player.find('2') > -1)):
                    print("Nie mozesz zbic swojej figury!")
                    time.sleep(3)
                    move(board, 8)
                elif(str(board[to_row][to_column]) == "  "):
                    print "Ruch na puste pole!"
                    board[to_row][to_column] = chosen_piece
                    board[piece_row][piece_column] = "  "
                    break #zepsute, gracz sie nie zmienia, moze dodac argument player do move'a
                else:
                    print "Zbito figure przeciwnika:", chosen_piece
                    board[to_row][to_column] = chosen_piece
                    board[piece_row][piece_column] = "  "
                    # to_piece.append(ch1osen_piece)
                    break
        else:
            print("Nie mozesz ruszac figury przeciwnika!")
            time.sleep(3)
            move(board, 8)
        #plansza_gracza[wiersz][kolumna] = teraz_odkryte_pole
		# if [piece_row, piece_column] in empty_fields:
		# 	print "To pole jest juz odkryte! Odkryj inne"
		# 	time.sleep(3)
		# elif teraz_odkryte_pole == 'X':
		# 	odkryte_pola.append([wiersz, kolumna])
		# 	os.system('cls')
		# 	wyswietl_plansze(plansza_oryginal, rozmiar_planszy)
		# 	print "\n"
		# 	wyswietl_plansze(plansza_gracza, rozmiar_planszy)
		# 	print "KONIEC GRY"
		# 	break
		# elif teraz_odkryte_pole == 0:
		# 	odkryte_pola.append([wiersz, kolumna])
		# 	plansza_gracza, odkryte_pola = odkryj_puste_pola(plansza_gracza, plansza_oryginal, odkryte_pola, rozmiar_planszy)
		# 	wyswietl_plansze(plansza_oryginal, rozmiar_planszy)
		# 	print "\n"
		# 	wyswietl_plansze(plansza_gracza, rozmiar_planszy)
		# else:
		# 	odkryte_pola.append([wiersz, kolumna])
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

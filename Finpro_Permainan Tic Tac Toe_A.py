from ast import Continue
from pickle import TRUE

print(" _______", "   _______", "   _______", "   _______", "   _______", "   _______", "   _______", "   _______", "   _______", "   _______" )
print("|   A   |", " |   Y   |", " |   O   |", " |       |", " |       |", " |       |", " |       |", " |       |", " |       |", " |       |")
print("|_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|")
print("|   B   |", " |   E   |", " |   R   |", " |   M   |", " |   A   |", " |   I   |", " |   N   |", " |       |", " |       |", " |       |")
print("|_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|")
print("|   T   |", " |   I   |", " |   C   |", " |       |", " |   T   |", " |   A   |", " |   C   |", " |       |", " |       |", " |       |")
print("|_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|")
print("|   T   |", " |   O   |", " |   E   |", " |       |", " |       |", " |       |", " |       |", " |       |", " |       |", " |       |")
print("|_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|")
print("|   M   |", " |   A   |", " |   D   |", " |   E   |", " |       |", " |   B   |", " |   Y   |", " |       |", " |       |", " |       |")
print("|_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|")
print("|   V   |", " |   A   |", " |   L   |", " |   L   |", " |   E   |", " |   N   |", " |   T   |", " |   I   |", " |   N   |", " |   O   |")
print("|_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|")
print("|   B   |", " |   E   |", " |   L   |", " |   A   |", " |   R   |", " |   D   |", " |   O   |", " |       |", " |       |", " |       |")
print("|_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|", " |_______|")
print("\n")






theBoard={'1': ' ', '2': ' ', '3': ' ',
     '4': ' ', '5': ' ', '6': ' ', 
     '7': ' ', '8': ' ', '9': ' '}

the_game_is_on=True
winner=None
turn='X'
options=['1', '2', '3', '4', '5', '6', '7', '8', '9']
import sys


def gaming_now():
	printBoard()
	while the_game_is_on:
		
		current_turn()

		check_if_game_over()

		change_turn()

	if winner == 'X' or winner == 'O':
		print("\n" + winner + " adalah juara			")
	else:
		print("\nImbang							")


def printBoard():
	print(theBoard['1']+ ' | ' +theBoard['2']+ ' | ' +theBoard['3'])
	print('---------')
	print(theBoard['4']+ ' | ' +theBoard['5']+ ' | ' +theBoard['6'])
	print('---------')
	print(theBoard['7']+ ' | ' +theBoard['8']+ ' | ' +theBoard['9'])

def current_turn():
	move=None
	import random
	if turn == 'X':
		print("Giliran " + turn + " Silahkan memmilih spot dari 1-9!")
		try:
			move=input()
		except KeyboardInterrupt:
			True
		while move not in theBoard.keys() or theBoard[move]!=' ':
			print("Itu sudah diisi," + ' coba pilih lagi!')
			try:
				move=input()
			except KeyboardInterrupt:
				continue

	elif turn=='O':
		print("Giliran " + turn + " Silahkan jalan\n")
		move=random.choice(options)
		while move not in theBoard.keys() or theBoard[move]!=' ':
			move = random.choice(options)

	print('Pemain ' + turn + ' pilih nomor ' + move +'.\n')
	theBoard[move]=turn
	printBoard()


def check_if_game_over():
	global the_game_is_on
	check_winner()
	if check_tie():
		the_game_is_on = False

def check_winner():
	global winner
	row_winner=check_rows()
	column_winner=check_columns()
	diagonal_winner=check_diagonals()
	if row_winner:
		winner=row_winner
	elif column_winner:
		winner=column_winner
	elif diagonal_winner:
		winner=diagonal_winner
	else:
		winner=None

def check_rows():
	global the_game_is_on
	row_1=theBoard['1']==theBoard['2']==theBoard['3']!=' '
	row_2=theBoard['4']==theBoard['5']==theBoard['6']!=' '
	row_3=theBoard['7']==theBoard['8']==theBoard['9']!=' '
	if row_1 or row_2 or row_3:
		the_game_is_on = False
	if row_1:
		return theBoard['1']
	elif row_2:
		return theBoard['4']
	elif row_3:
		return theBoard['5']
	else:
		return None


def check_columns():
	global the_game_is_on
	column_1=theBoard['1']==theBoard['4']==theBoard['7']!=' '
	column_2=theBoard['2']==theBoard['5']==theBoard['8']!=' '
	column_3=theBoard['3']==theBoard['6']==theBoard['9']!=' '
	if column_1 or column_2 or column_3:
		the_game_is_on=False
	if column_1:
		return theBoard['1']
	elif column_2:
		return theBoard['2']
	elif column_3:
		return theBoard['3']
	else:
		return None

def check_diagonals():
	global the_game_is_on
	dig_1=theBoard['1']==theBoard['5']==theBoard['9']!=' '
	dig_2=theBoard['3']==theBoard['5']==theBoard['7']!=' '
	if dig_1 or dig_2:
		the_game_is_on = False
	if dig_1:
		return theBoard['1']
	elif dig_2:
		return theBoard['3']
	else:
		return None

def check_tie():
	if " " in theBoard.values():
		return False
	else:
		return True


def change_turn():
	global turn

	if turn=='X':
		turn='O'
	else:
		turn='X'



gaming_now()



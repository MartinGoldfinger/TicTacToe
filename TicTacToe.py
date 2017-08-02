"""
Tic Tac Toe game found on /r/Python
Modified from:
https://www.reddit.com/r/Python/comments/6qvu38/my_code_for_tictactoe_beginner_compared_to_my/
"""

import sys

class Player:
	"""
	Functions:
		__init__ : assign the name, symbol, initialize variables
		winner_check : Checks the board for a winner
		player_move : user enters board position, will check for valid location
		clear_board : reset self.board list

	Attributes:
		name (str) - player name
		symbol (char) - player symbol, X or O
		board (list) - stores user moves
		win_count (int) - Number of times player has won a round
	"""

	def __init__(self, symbol):
		self.name = input("Enter your name: ")
		self.symbol = symbol
		self.board = []
		self.win_count = 0

	def player_move(self):
		"""
		Player enters position on grid and validates and populates
		"""
		while True:
			move = input("{0.name}'s ( {0.symbol} ) turn, please choose placement (1-9): ".format(self))
			if move in ('1', '2', '3', '4', '5', '6', '7', '8', '9') and (int(move) not in game_list):
				self.board.append(int(move))
				game_list.append(int(move))
				position[int(move)-1] = (self.symbol)
				print_board()
				break #When a valid move is made get out of the loop and function

			elif move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
				print('That is not a valid move! Try again')
			else:
				print('That move is taken!, Try again')

	def winner_check(self):
		"""
		Returns Boolean - Checks player's board list for 3 in a row, column or diagonal
		"""
		if (1 in self.board) and (2 in self.board) and (3 in self.board) or \
			(4 in self.board) and (5 in self.board) and (6 in self.board) or \
			(7 in self.board) and (8 in self.board) and (9 in self.board) or \
			(1 in self.board) and (4 in self.board) and (7 in self.board) or \
			(2 in self.board) and (5 in self.board) and (8 in self.board) or \
			(3 in self.board) and (6 in self.board) and (9 in self.board) or \
			(1 in self.board) and (5 in self.board) and (9 in self.board) or \
			(3 in self.board) and (5 in self.board) and (7 in self.board):
				print('{0.name} wins as {0.symbol}.'.format(self))
				self.win_count += 1
				return True
		else:
			return False

	def clear_board(self):
		"""
		Clearing board used in reseting rounds
		"""
		self.board = []

#End of Player class


def print_board():
	"""
	Prints current board and position guide
	"""
	print('')
	print(' '+ position[0] +' | '+ position[1] +' | '+ position[2] + ' ' * 10 + '1' +' | '+ '2' +' | '+ '3')
	print('-' * 11 + ' ' * 8 + '-' * 11)
	print(' '+ position[3] +' | '+ position[4] +' | '+ position[5] + ' ' * 10 + '4' +' | '+ '5' +' | '+ '6')
	print('-' * 11 + ' ' * 8 + '-' * 11)
	print(' '+ position[6] +' | '+ position[7] +' | '+ position[8] + ' ' * 10 + '7' +' | '+ '8' +' | '+ '9')
	print('')
#End of print_board function

"""
Start main game
"""
play_game = True
print ('Welcome to Tic Tac Toe.')

print("Player 1", end=' ')
player_one = Player('X')

print("Player 2", end=' ')
player_two = Player('O')

print("Player 1 is {0.name} using {0.symbol} and Player 2 is {1.name} using {1.symbol}".format(player_one, player_two))
input("Press Enter to continue...")

while play_game:
	position = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	game_list = []
	move_count = 0
	winner = False

	print_board()

	#Game round loop, alternates based on move_count
	while (move_count < 9) and (winner is False):
		if move_count % 2 == 0:
			player_one.player_move()
			winner = player_one.winner_check()
		else:
			player_two.player_move()
			winner = player_two.winner_check()
		move_count += 1


	if winner == True:
		print('Congrats!')
	else:
		print('Its a tie!')

	print('')
	print('Current score: {0.name} has {0.win_count} and {1.name} has {1.win_count}'.format(player_one, player_two))
	print('')

	#play again loop, validates user input
	while True:
		play_again = input('Play again? (y/n)')

		if play_again == 'y':
			print('Resetting...')
			player_one.clear_board()
			player_two.clear_board()
			break #breaking play again input loop

		elif play_again == 'n':
			print('Thanks for playing!')
			sys.exit()
		else:
			print('answer not valid, please use y or n')


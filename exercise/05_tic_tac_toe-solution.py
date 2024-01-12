import time


def print_game_field(game_field):
	print("   1 2 3\n  -------")
	a = 1
	for row in game_field:
		print(str(a) + "|", end=" ")
		a += 1
		for cell in row:
			print(cell, end=' ')
		print("")


def count_free_cells(game_field):
	count = 0
	for row in game_field:
		for cell in row:
			if cell == '':
				count += 1
	return count


def select_field(game_field, player):
	selected = False
	while not selected:
		row = int(input("Select row: "))
		col = int(input("Select column: "))
		if row < 1 or row > 3 or col < 1 or col > 3:
			print("Invalid input. Try again.")
			continue
		if game_field[row - 1][col - 1] == '':
			game_field[row - 1][col - 1] = player
			selected = True
		else:
			print("Field already selected. Try again.")


def check_winner(game_field):
	# Horizontal
	for i in range(3):
		if game_field[i][0] == game_field[i][1] == game_field[i][2] != '':
			return game_field[i][0]
	# Vertical
	for i in range(3):
		if game_field[0][i] == game_field[1][i] == game_field[2][i] != '':
			return game_field[0][i]

	# Diagonal
	if game_field[0][0] == game_field[1][1] == game_field[2][2] != '':
		return game_field[0][0]
	if game_field[0][2] == game_field[1][1] == game_field[2][0] != '':
		return game_field[0][2]
	return None


def game_move(game_field, player):
	select_field(game_field, player)
	winner = check_winner(game_field)
	if winner is not None:
		print_spacer()
		print_game_field(game_field)
		print("Game finished. Winner is " + winner + "!")
		exit(0)


def print_spacer():
	print("\n" * 20)


field = [
	['', '', ''],
	['', '', ''],
	['', '', '']
]

game_finished = False
current_player = 'X'
while not game_finished:
	if count_free_cells(field) == 0:
		print("Game finished. DRAW!")
		game_finished = True
		continue
	game_move(field, current_player)
	current_player = 'X' if current_player == 'O' else 'O'
	print_spacer()
	print_game_field(field)

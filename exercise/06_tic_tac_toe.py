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


def print_spacer():
	print("\n" * 20)


field = [
	['X', 'O', 'X'],
	['O', 'X', 'O'],
	['X', 'O', 'X']
]

while True:
	print_spacer()
	print_game_field(field)
	time.sleep(1)

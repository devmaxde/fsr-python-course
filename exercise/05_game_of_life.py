import random
import time

size = 30
field_char = "◾"

field = [
	['' for _ in range(size)] for _ in range(size)
]


def print_game_field(game_field):
	print("   " + " ".join(
		[str(x) if x >= 10 else "0" + str(x) for x in range(1, len(game_field[0]) + 1)]) + "\n   " + "-" * 3 * len(
		game_field[0]))
	a = 1
	for row in game_field:
		b = str(a) if a >= 10 else "0" + str(a)
		print(b + "|", end=" ")
		a += 1
		for cell in row:
			if cell == '':
				cell = ' '
			print(cell, end='  ')
		print("")


def print_spacer():
	print("\n" * 20)


def randomize_field(local_field):
	for a in range(len(local_field)):
		for b in range(len(local_field[a])):
			local_field[a][b] = field_char if random.randint(0, 1) == 1 else ''
	return local_field


def calculate_next_generation(local_field):
	return local_field


field = randomize_field(field)

while True:
	field = calculate_next_generation(field)
	print_spacer()
	print_game_field(field)
	time.sleep(1)

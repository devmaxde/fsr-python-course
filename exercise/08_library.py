from typing import List
from book import Book


class Library:
	__books: List[Book]

	def __init__(self, name):
		self.name = name
		self.__books = []


while True:
	print("Welcome to the library")
	print("Pick one of the Following options:")
	options = ["Add new book", "List all books", "Search for book", "Exit"]
	for i in range(len(options)):
		print(f"{i +1 }: {options[i]}")
	user_input = input()
	if user_input == "1":
		# input values
		# create book object
		# add book object to library
		print("Add new book")
	elif user_input == "2":
		print("List all books")
	elif user_input == "3":
		author = input("Enter author: ")
		# TODO search for book
		print("Search for book")
	elif user_input == "4":
		print("Exit")
		break
	else:
		print("Invalid input. Try again.")

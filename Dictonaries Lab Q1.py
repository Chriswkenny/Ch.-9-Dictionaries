#Christopher Kenny
#CS 175
#Dictonaries Lab Q1. Create a program that will store book and display all books using dictionaries.

book_log = {}

def main_menu():
  while True:
    print("Birthday Manager: ")
    print("1. Add a Book")
    print("2. Display all Books")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      add_book()

    elif choice == 2:
      view_all_books()

    elif choice == 3:
      print("Goodbye!")
      break

    else:
      print('Invalid')

def add_book():
  book = input("Enter the Book Title: ").title()
  book_log[book] = "Available"
  print(f'The book "{book}" has been added to the library.')
  print(" ")

def view_all_books():
  print(" ")
  print("Library Books:")
  for book, status in book_log.items():
    print(f"{book}: {status}")
  print(" ")


main_menu()


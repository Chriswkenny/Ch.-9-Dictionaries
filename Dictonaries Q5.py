#Christopher Kenny
#CS 175
#Dictionaries Q5: Create a program to store friend’s name and birthdate in a dictionary object using input().

birthdays = {}

def main_menu():
  while True:
    print("Birthday Manager: ")
    print("1. Add a Birthday")
    print("2. View a Birthday")
    print("3. Display All Birthdays")
    print("4. Quit")
    print(" ")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      add_birthday()

    elif choice == 2:
      view_birthday()

    elif choice == 3:
      display_all()

    elif choice == 4:
      print("Goodbye!")
      break

    else:
      print('Invalid')


def add_birthday():
  name = input("Enter a name: ")
  birthday = input("Enter a birthday (EX: YYYY-MM-DD): ")
  birthdays[name] = birthday
  print(f"{name}'s birthday has been added!")
  print(" ")


def view_birthday():
  name = input("Enter the name of the person who you want to look up: ")
  if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}")
    print(" ")
  else:
    print(f"Nobody found named {name} in system.")
    print(" ")

def display_all():
  for name, birthday in birthdays.items():
    print(f"{name}: {birthday}")
  print(" ")


main_menu()

#Christopher Kenny
#CS 175
#Dictonaries Q1: Create a program that will print only the names of people who live in chicago using list comprehension

persons = {
    'Danny': 'New York',
    'Ben': 'New Jersey',
    'Bob': 'Chicago',
    'Tom': 'Houston',
    'Sam': 'Phoenix',
    'Tim': 'Philadelphia',
    'Nancy': 'Chicago'
}

chicago_people = [name for name, city in persons.items() if city == 'Chicago']
print(chicago_people)

#Christopher Kenny
#CS 175
#Dictonaries Q2: Given a dictionary, create a new dictionary where keys and values are swapped

original = {'Math': 'Alice', 'Science': 'Bob', 'History': 'Charlie'}

swapped = {value: key for key, value in original.items()}
print(swapped)

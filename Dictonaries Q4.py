#Christopher Kenny
#CS 175
#Dictionaries Q4: Create a program to combine two dictionaries, summing values for common keys

combined_dict = {}

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 5, 'd': 50}

for key in dict1:
  combined_dict[key] = dict1[key]

for key in dict2:
  if key in combined_dict:
    combined_dict[key] += dict2[key]
  else:
    combined_dict[key] = dict2[key]

print(combined_dict)

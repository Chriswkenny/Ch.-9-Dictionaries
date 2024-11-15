#Christopher Kenny
#CS 175
#Sets Q1: Create a program that demonstrates various set operations

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

#Baseball Team
print("The following students are on the baseball team: ")
for person in baseball:
  print(person)

#Basketball Team
print('')
print("The following students are on the basketball team: ")
for person in basketball:
  print(person)

#Students playing both Baseball and Basketball
print('')
print("The following students play both baseball and basketball: ")
for person in baseball.intersection(basketball):
  print(person)

#Students playing either baseball or basketball
print('')
print('The following students play either baseball or basketball: ')
for person in baseball.union(basketball):
  print(person)

#Students playing baseball but not basketball
print('')
print('The following students play baseball, but not basketball: ')
for person in baseball.difference(basketball):
  print(person)

#Students playing basketball but not baseball
print('')
print('The following students play basketball, but not baseball: ')
for person in basketball.difference(baseball):
  print(person)

#Students playing one sport, but not both
print('')
print('The following students play one sport, but not both: ')
for person in baseball.symmetric_difference(basketball):
  print(person)

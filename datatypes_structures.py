# ENGIN480 -  Special Topics: Introduction to Computational Modeling for Renewable Energy
# Instructor: Rafael Valotta Rodrigues
# March 25th, 2025

# 1. Lists
books = ['1984', '100 years of soletude', 'Blindness']
numbers = [0, 2.309823498, 399329382]

# 1.1 printing the list
print(books)

# 1.2 looping over it and printing each element
for i in books:
    print(i)

# or

for k in range(len(books)):
    print('Book:',books[k])


# 1.3 Replacing an element of the list:
# 
#  
print('starting replacement on list')

for k in range(len(books)):
    if books[k] == 'Blindness':
        books[k] = 'Notes From Underground'
    print('Book:',books[k])

# 2. Tuples
numbers = (1, 4, 18, 20, 37, 70)

# 2.1 printing the list
print(numbers)

# 2.2 Looping over it and printing each element
for k in range(len(numbers)):
    print(k)


# 2.3 Attempting to replace an element from a tuple:
print('starting attempt to replace element on tuple')

for k in range(len(numbers)):
    if numbers[k] == 18:
        # numbers[k] = 19
        pass
    print('Number:', numbers[k])
# it is not possible to replace elements in tuples, therefore there will be a bug here
 

# 3. Dictionaries
tasks = {'morning'  :'wash', 
         'lunch'    : 'walk the dog', 
         'afternoon': 'go to school', 
         'evening'  : 'workout'}

print('')

print('starting dictionaries')

print(tasks.keys())

print(tasks.get('morning'))
print(tasks.get('lunch'))
print(tasks.get('afternoon'))
print(tasks.get('evening'))

#or

print(tasks.keys().mapping['morning'])
print(tasks.keys().mapping['lunch'])
print(tasks.keys().mapping['afternoon'])
print(tasks.keys().mapping['evening'])


print('done')
print('done')

#testing my code

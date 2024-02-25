"""
CP1404/CP5632 Practical
List comprehensions
Name: Arun Parajuli
"""

# Original names list
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]

# Original full names list
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# List comprehension to get the first letter of each name
first_initials = [name[0] for name in names]
print(first_initials)

# List comprehension to get the first letter of each name (alternative approach)
first_initials = [name[0] for name in names]
print(first_initials)

# List comprehension to get the initials of each full name
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# List comprehension to get lowercase versions of full names
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# List comprehension to convert strings to integers
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(number) for number in almost_numbers]
print(numbers)

# List comprehension to filter numbers greater than 9
numbers_greater_than_9 = [number for number in numbers if number > 9]
print(numbers_greater_than_9)

# List comprehension to get last names longer than 11 characters
long_last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_last_names)

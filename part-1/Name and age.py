# Ask the user for a name and his birth year
# Print out as shown in example below:
# Birth year is 1990
# Hi Name Surname, you will be 31 years old at the end of year 2021

name = input("What is your name? ")
birth_year = int(input("Which year were you born? "))

print(f"Hi {name}, you will be {2021 - birth_year} years old at the end of the year 2021")

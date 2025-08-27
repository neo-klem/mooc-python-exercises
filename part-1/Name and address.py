# Ask user for a name, his family name, street andress, city and postal code.
# It should be printed as in following example:

# Steve Sanders
# 91 Station Road
# London EC05 6AW

name = input("Given name: ")
family_name = input("Family name: ")
street_address = input("Street address: ")
city_and_postal = input("City and postal code: ")

print(f"{name} {family_name}\n{street_address}\n{city_and_postal}")

# We prompted the user for variables and used them in an f-string.
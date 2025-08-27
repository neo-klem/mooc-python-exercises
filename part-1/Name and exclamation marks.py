# Ask user for their name and then print is as shown below:
# !name!name!
# name is a variable we use for prompting the user.

name = input("What is your name? ")

print(f"!{name}!{name}!")

# We used an f-string so that we don't need to add so much + and " ".

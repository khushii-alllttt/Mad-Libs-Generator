print("🎉 Welcome to Mad Libs Generator! 🎉")
print("Fill in the blanks to create your funny story.\n")

# Collect user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a type of food: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")

# Story template
story = f"""
One day, {name} went to {place}.  
There they saw a {adjective} {animal} eating {food}.  
{ name } was so surprised that they started to {verb} loudly!  
It was the funniest day ever!
"""

print("\nYour Mad Lib Story:")
print(story)

""" 
Create a tuple named zoo that contains 10 of your favorite animals.
"""

zoo = ("cat", "dragon", "thestral", "unicorn", "raven", "eevee", "fox", "rabbit", "ninja turtle (any age)", "thundercat")

""" 
Find one of your animals using the tuple.index(value) syntax on the tuple.
"""

print(zoo.index("raven"))

"""
Determine if an animal is in your tuple by using value in tuple syntax.
"""
animal_to_find = "dragon"
if animal_to_find in zoo:
    print(f"Here's your {animal_to_find}!")
else:
    print(f"We're sorry, but your {animal_to_find} escaped.")

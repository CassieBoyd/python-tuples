# Tuples are like lists, but are immutable. They can't be modified once defined.

""" 
Create a tuple named zoo that contains 10 of your favorite animals.
"""

zoo = ("cat", "dragon", "thestral", "unicorn", "raven", "eevee", "fox", "rabbit", "ninja turtle (any age)", "thundercat")

""" 
Find one of your animals using the tuple.index(value) syntax on the tuple.
"""
# use .index() to find the index of an item in a tuple
print(zoo.index("raven"))

"""
Determine if an animal is in your tuple by using value in tuple syntax.
"""
# "in" keyword is used to check for a value in the tuple, it returns a boolean and triggers the appropriate code to execute.
animal_to_find = "dragon"
if animal_to_find in zoo:
    print(f"Here's your {animal_to_find}!")
else:
    print(f"We're sorry, but your {animal_to_find} escaped.")

"""
You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
children = ("Sally", "Hansel", "Gretel", "Svetlana")
(first_child, second_child, third_child, fourth_child) = children
print(first_child) # Output is "Sally"
print(second_child) # Output is "Hansel"
print(third_child) # Output is "Gretel"
print(fourth_child) # Output is "Svetlana"

Create a variable for the animals in your zoo tuple, and print them to the console.
"""

# Unpacking a tuple into another tuple by having the variable on the right side of the equal sign.
(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal,ninth_animal, tenth_animal) = zoo

# print(third_animal)
print(zoo)

"""
Convert your tuple into a list.
"""

zoo_list = [item for item in zoo] 
print("ZOO LIST", zoo_list)

zoo_too = list(zoo)
print(list(zoo_too))

"""
Use extend() to add three more animals to your zoo.
"""
# Use parentheses and square brackets with extend when adding multiple items.
zoo_too.extend(["raccoon", "skunk", "opossum"])
print(zoo_too)

"""
Convert the list back into a tuple.
"""

def convert(zoo_too): 
    return tuple(zoo_too)

print(convert(zoo_too))

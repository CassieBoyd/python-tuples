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

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal,ninth_animal, tenth_animal) = zoo

# print(third_animal)
print(zoo)

"""
Convert your tuple into a list.
"""

# zoo_list = [item for item in zoo] 
# print(zoo_list)

list(zoo)
print(list(zoo))

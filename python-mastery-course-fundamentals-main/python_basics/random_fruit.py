from random import choice

items = ["apple", "banana", "mangoes"]


def rand_fruit(fruits):
    if not fruits:
        return "The fruit list is empty"
    return choice(fruits)


fruit = rand_fruit(items)
print(f"The Random fruit is: {fruit}")

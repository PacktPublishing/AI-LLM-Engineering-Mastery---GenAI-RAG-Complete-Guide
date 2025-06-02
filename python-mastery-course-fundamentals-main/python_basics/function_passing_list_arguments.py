plants = ["lemon-tree", "mango-tree", "apple-tree"]


def water_plants(plants):
    for plant in plants:
        action = f"Watering the {plant}."
        print(action)


water_plants(plants=plants)

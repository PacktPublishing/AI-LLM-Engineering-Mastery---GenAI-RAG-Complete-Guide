class Vehicle:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.year} {self.name}"


# Define a subclass of Vehicle
class Car(Vehicle):
    def __init__(self, name, year, mileage):
        super().__init__(name, year)  # Call to the superclass (Vehicle) __init__
        self.mileage = mileage

    def __str__(self):
        return f"{super().__str__()} with {self.mileage} miles"


print(issubclass(Vehicle, object))
print(issubclass(Car, object))

print(Vehicle.__bases__)
print(Car.__bases__)

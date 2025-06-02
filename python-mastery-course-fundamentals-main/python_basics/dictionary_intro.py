person = {"name": "Alex", "age": 34, "city": "New York"}

person.pop("age")
person.popitem()
del person["is_employed"]
person.clear()

print(person)

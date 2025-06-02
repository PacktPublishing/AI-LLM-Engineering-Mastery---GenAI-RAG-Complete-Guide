person = {"name": "Alex", "age": 34, "city": "New York"}

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key} -> {value}")

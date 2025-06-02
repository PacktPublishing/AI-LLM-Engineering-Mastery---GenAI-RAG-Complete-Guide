family = {"mom": {"name": "Gina", "age": 78}, "dad": {"name": "Maba", "age": 89}}
for name, information in family.items():
    print(f"\nParent type:{name}")
    parent_name = f"Name: {information["name"]}"
    parent_age = f"Age: {information["age"]}"
    
    print(f"\n {parent_name}")
    print(f"\n {parent_age}")

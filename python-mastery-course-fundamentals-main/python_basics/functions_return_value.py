def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


formatted_name = format_name(first_name="james", last_name="bond")
print(formatted_name)

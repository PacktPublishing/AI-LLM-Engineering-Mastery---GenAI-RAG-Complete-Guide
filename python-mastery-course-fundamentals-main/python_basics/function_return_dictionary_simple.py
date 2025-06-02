def build_profile(first, last):
    """Build a dictionary containing everything we know about a user"""

    user = {"first": first, "last": last}
    return user


user = build_profile("Gina", "Kibo")
print(user)

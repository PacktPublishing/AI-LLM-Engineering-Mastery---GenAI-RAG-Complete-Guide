def sum_numbers(*args):
    return sum(args)


def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


print(build_profile("James", "Bond", location="UK", age=57, field="movies"))

# print(f"The sum:: {sum_numbers(2, 45, 1, 34, 89, 10)}")

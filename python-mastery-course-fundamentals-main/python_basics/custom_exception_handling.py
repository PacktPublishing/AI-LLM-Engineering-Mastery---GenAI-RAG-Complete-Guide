class MyCustomError(Exception):
    pass


class ValueTooSmallError(MyCustomError):
    pass


class ValueTooLargeError(MyCustomError):
    pass


def check_value(number):
    if number < 5:
        raise ValueTooSmallError(f"The number {number} is to small.")
    elif number > 15:
        raise ValueTooLargeError(f"The number {number} is too large")
    else:
        print(f"The number {number} is within the allowed range.")


try:
    user_input = int(input("Enter a number"))
    check_value(user_input)
except ValueTooSmallError as e:
    print(e)
except ValueTooLargeError as e:
    print(e)

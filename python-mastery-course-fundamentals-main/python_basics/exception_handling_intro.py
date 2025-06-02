# Exceptions
try:
    print(12 / 0)
except ZeroDivisionError as e:
    print(f"Error ocurred: {e}")
else:
    print("All is well here")
finally:
    # code to clean up resources
    print("No matter what, I'll execute!")

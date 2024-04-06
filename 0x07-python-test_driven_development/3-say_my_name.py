def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    print(f"My name is {first_name} {last_name}")

# Example usage:
try:
    say_my_name("John", "Doe")
    say_my_name("Jane")
except TypeError as e:
    print(e)


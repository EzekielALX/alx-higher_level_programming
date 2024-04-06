def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print('#' * size)

# Example usage:
try:
    print_square(3)
except (TypeError, ValueError) as e:
    print(e)


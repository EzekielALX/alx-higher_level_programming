def add_integer(a, b=98):
    
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ['.', '?', ':']
    start = 0
    
    for i, char in enumerate(text):
        if char in special_chars:
            print(text[start:i + 1].strip())
            print()
            start = i + 1
    print(text[start:].strip())  # Print the remaining text after the last special character

# Example usage:
try:
    text = "Hello? Is it me you're looking for. I can see it in your eyes. I can see it in your smile:"
    text_indentation(text)
except TypeError as e:
    print(e)


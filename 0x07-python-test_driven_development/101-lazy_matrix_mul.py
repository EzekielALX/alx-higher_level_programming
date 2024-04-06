import numpy as np

def lazy_matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]] or not all(row for row in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or not all(row for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    try:
        result = np.dot(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e

    return result

# Example usage:
try:
    m_a = [[1, 2], [3, 4]]
    m_b = [[5, 6], [7, 8]]
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)


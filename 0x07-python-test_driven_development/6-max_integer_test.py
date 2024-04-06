import unittest
# The function to be tested
def max_integer(list=[]):
    if len(list) == 0:
        return None
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num
    return max_num

# The unittest class
class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        """Test with the max integer at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with the max integer in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 2]), 4)

    def test_one_negative(self):
        """Test with a list that includes negative numbers"""
        self.assertEqual(max_integer([-2, -3, -1]), -1)

    def test_all_negative(self):
        """Test with a list of all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list that has one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_ints_and_floats(self):
        """Test with a list of integers and floats"""
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_string(self):
        """Test with a list that contains a string"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three"])

    def test_none(self):
        """Test with None as an input"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()


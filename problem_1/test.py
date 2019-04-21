import unittest
from problem_1.solution import check

class HelloTest(unittest.TestCase):

    def test_empty_array(self):
        self.assertFalse(check([], 3))
    
    def test_array_one_element(self):
        self.assertFalse(check([1], 2))
        self.assertTrue(check([1], 1))
    
    def test_array_two_elements(self):
        self.assertFalse(check([1, 2], 2))
        self.assertTrue(check([1, 1], 2))
    
    def test_array_greater_two_elements(self):
        self.assertFalse(check([1, 1, 1], 3))
        self.assertFalse(check([1, 2, 3], 2))
        self.assertFalse(check([1, 2, 3, 4], 8))
        self.assertFalse(check([1, 2, 3, 4, 7, 0, 7, 9], 100))

        self.assertTrue(check([1, 1, 1], 2))
        self.assertTrue(check([1, 2, 3, 4], 7))
        self.assertTrue(check([1, 2, 3, 4, 7, 0, 7, 9], 1))
    
if __name__ == '__main__':
    unittest.main()
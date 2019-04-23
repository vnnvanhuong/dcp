import unittest
from problem_4.solution import find

class TestProblem4(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(find([3, 4, -1, 1]), 2)

    def test_case_1(self):
        self.assertEqual(find([1, 2, 0]), 3)
    
if __name__ == '__main__':
    unittest.main()

import unittest
from problem_2.solution import newArr, optimizedNewArr

class TestProblem2(unittest.TestCase):

    def test_case_1(self):
        self.assertEquals(newArr([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    
    def test_case_2(self):
        self.assertEquals(newArr([3, 2, 1]), [2, 3, 6])


    def test_case_3(self):
        self.assertEqual(optimizedNewArr([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    
    def test_case_4(self):
        self.assertEquals(optimizedNewArr([3, 2, 1]), [2, 3, 6])

if __name__ == '__main__':
    unittest.main()
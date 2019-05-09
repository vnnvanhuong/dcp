import unittest

from problem_7.solution import count

class TestProblem7(unittest.TestCase):

    def test_len_1(self):

        self.assertEqual(count('1'), 1)
        self.assertEqual(count('9'), 1)
    
    def test_len_2(self):

        self.assertEqual(count('11'), 2)
        self.assertEqual(count('12'), 2)
        self.assertEqual(count('13'), 2)
        self.assertEqual(count('32'), 1)
    
    def test_len_greater_than_2(self):

        self.assertEqual(count('111'), 3)
        self.assertEqual(count('121'), 3)
        self.assertEqual(count('131'), 2)
        self.assertEqual(count('321'), 2)
        self.assertEqual(count('333'), 1)
        self.assertEqual(count('1234'), 3) # 12, 23
        self.assertEqual(count('34562132'), 3) # 21, 13

    
if __name__ == '__main__':
    unittest.main()

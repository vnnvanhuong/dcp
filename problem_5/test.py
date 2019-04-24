import unittest
from problem_5.solution import cons, car, cdr

class TestProblem5(unittest.TestCase):

    def test_car(self):
        self.assertEqual(car(cons(3, 4)), 3)

    def test_cdr(self):
        self.assertEqual(cdr(cons(3, 4)), 4)
    
if __name__ == '__main__':
    unittest.main()

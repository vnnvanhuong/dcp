import unittest

from problem_6.solution import XorLinkedList

class TestProblem6(unittest.TestCase):

    def test_case_1(self):
        l = XorLinkedList()

        for i in range(0, 4):
            l.add(i)
        
        self.assertEqual(l.get(2), 2)

    
if __name__ == '__main__':
    unittest.main()

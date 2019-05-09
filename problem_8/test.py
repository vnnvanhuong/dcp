import unittest

from problem_8.solution import Node, count_unival_subtrees

class TestProblem8(unittest.TestCase):

    def test_case_1(self):
        root = Node(0, Node(1, None, None), Node(0, Node(1, Node(1, None, None), Node(1, None, None)), Node(0, None, None)))
        
        self.assertEqual(5, count_unival_subtrees(root))

    
if __name__ == '__main__':
    unittest.main()

import unittest
from problem_3.solution import Node, deserialize, serialize

class TestProblem3(unittest.TestCase):

    def test_case_0(self):
        node = Node('root')
        self.assertEqual(deserialize(serialize(node)).val, 'root')
    
    def test_case_1(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')
    
    def test_case_2(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).right.val, 'right')
    
    def test_case_3(self):
        node = Node('root', Node('left', Node('left.left')))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')
    
    # def test_case_4(self):
    #     node = Node('root', None, Node('right', Node('right.right')))
    #     self.assertEqual(deserialize(serialize(node)).right.right.val, 'right.right')

    # def test_case_5(self):
    #     node = Node('root', Node('left', Node('left.left')), Node('right', Node('right.right')))
    #     self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')
    #     self.assertEqual(deserialize(serialize(node)).right.right.val, 'right.right')
    
if __name__ == '__main__':
    unittest.main()

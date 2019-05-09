class Node(object):
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def count_unival_subtrees(root: Node):
    # if root is none --> 0
    # else count = 1 if root is a unival tree
    # recursive for left node and right node
    if root is None:
        return 0

    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    
    return 1 + left + right if is_unival(root) else left + right
    



def  is_unival(root):
    # all left values == all right values == root value
    return helper(root, root.value)

def helper(node, value):

    if node is None:
        return True
    
    if node.value == value:
        return helper(node.left, value) and helper(node.right, value)
    
    return False
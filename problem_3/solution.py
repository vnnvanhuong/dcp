class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def deserialize(nodeStr: str) -> Node:
    """
    construct Node from the format
    root{left{left.left},right}
    """
    
    nodes = nodeStr.split("{", 1)

    node = None
    if (len(nodes) == 1):
        node = Node(nodes[0])
    else:
        if (nodes[1].find(',') < 0):
            node = Node(nodes[0], deserialize(nodes[1].replace('}', '')))
        else:
            parts = nodes[1].split(',', 1)
            left = parts[0].replace('}', '')
            right = parts[1].replace('}', '')
            node = Node(nodes[0], deserialize(left), deserialize(right))

    return node
    


def serialize(node: Node) -> str:
    """
    parse to the following format
    root{left{left.left},right}
    """
    result = node.val
    if (node.left == None and node.right == None):
        return result
    else:
        if (node.left != None and node.right == None):
            result += '{' + serialize(node.left) + '}'
        
        if (node.right != None and node.left == None):
            result +=  '{' + serialize(node.right) + '}'
        
        if (node.left != None and node.right != None):
            result += '{' + serialize(node.left) + ',' + serialize(node.right) + '}'
    
    return result
    

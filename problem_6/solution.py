# Ref: https://github.com/r1cc4rdo/daily_coding_problem

class Node(object):
    
    def __init__(self, value, prev_index, next_index):
        self.value = value
        self.both = prev_index ^ next_index
    
    def getNext(self, prev_index):
        return self.both ^ prev_index
    
    def getPrev(self, next_index):
        return self.both ^ next_index

class XorLinkedList(object):

    def __init__(self):
        self.memory = [Node(None, -1, -1)] # head

    def head(self):
        return 0, -1, self.memory[0] # current node index, previsous node index, current node
    
    def add(self, value):
        """
        adds the element to the end
        """
        # get head
        current_index, prev_index, current_node = self.head()
        
        # find tail
        while(True):
            next_index = current_node.getNext(prev_index)

            if (next_index == -1):
                break
            
            current_index, prev_index = next_index, current_index
            current_node = self.memory[next_index]
        
         # update tail
        new_index = len(self.memory)
        current_node.both = prev_index ^ new_index
        self.memory.append(Node(value, current_index, -1))
    
    def get(self, index):
        """
        returns the node at index
        """
        # get head
        current_index, prev_index, current_node = self.head()
       
        # find and return node at index
        for i in range(index + 1):
            current_index, prev_index = current_node.getNext(prev_index), current_index
            current_node = self.memory[current_index]
        
        return current_node.value
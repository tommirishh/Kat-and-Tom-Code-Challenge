#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root, string):        
        if not root:
            string.append('#')
            return
        string.append(root.val)
        self.serialize(root.left, string)
        self.serialize(root.right, string)
        return(string)


    def deserialize(self, s):
        i = 0
        if s[i] == '#':
            i += 1
            return None
        value = s[i]
        i += 1
        left = node.deserialize(s)
        right = node.deserialize(s)
        return Node(value, left, right)

node = Node('root', Node('left', Node('left.left')), Node('right'))

string = []

print node 
#print(node.deserialize(node.serialize(node, string)).left.left.val)
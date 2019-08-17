class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_node(self, value):
        if self.root == None:
            self.root = Node(value, None, None)
        else:
            self.int_insert(value=value, node=self.root, parent=None, branch=0)

    def int_insert(self, value, node, parent, branch):
        if (node == None):
            node = Node(value, None, None)
            if branch == 0: 
                parent.left = node
            else:
                parent.right = node
        else:
            if (value < node.value):
                self.int_insert(value, node.left, node, 0)
            else:
                self.int_insert(value, node.right, node, 1)
    
    def traverse(self, node):
        if (node != None):
            self.traverse(node.left)
            print(node.value)
            self.traverse(node.right)

    def min_internal(self, node):
        if node == None:
            return None
        if node.left != None:
            return self.min_internal(node.left)
        else:
            return node.value
    
    def min(self):
        return self.min_internal(self.root)
        

            

    def print_tree(self):
        self.traverse(self.root)
    
    def internal_search(self, node, value):
        if ( node != None ):
            if ( node.value == value ):
                return value
            if ( value < node.value ):
                self.internal_search(node.left, value)
            else:
                self.internal_search(node.right, value)
            

    def search(self, value):
        return self.internal_search(self.root, value)


tree = BinaryTree()
tree.insert_node(75)
#print("root is not null" if tree.root != None else "root is null")
tree.insert_node(100)
tree.insert_node(50)
tree.insert_node(1)
tree.insert_node(-200)
print(tree.search(75))
print("Min: " + str(tree.min()))
#tree.print_tree()
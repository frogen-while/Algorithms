class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.key)

class BinarySearchTree:
    def __init__(self, key):
        self.root = Node(key)
        
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, cur_node, key):
        if cur_node is None:
            return Node(key)
        else:
            if key < cur_node.key:
                cur_node.left = self._insert_recursive(cur_node.left, key)
            else:
                cur_node.right = self._insert_recursive(cur_node.right, key)
        return cur_node
    
    def in_order(self):
        return self._in_order_recursive(self.root)
    
    def _in_order_recursive(self, root):
        result = []
        if root == None:
            return
        self._in_order_recursive(root.left)
        result.append(root)
        self._in_order_recursive(root.right)
        return result

    def get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def search(self, target):
        return self._find_recursive(target, self.root)

    def _search_recursive(self, target, node):
        if node is None:
            return False
        if node.key == target:
            return True
        if target > node.key:
            return self._find_recursive(target, node.right)
        else:
            return self._find_recursive(target, node.left)
    
        
tree = BinarySearchTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
print(tree.find(1))

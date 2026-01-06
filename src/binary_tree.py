from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.key)

class BinaryTree:
    def __init__(self):
        self.root = None

    def InsertNode(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        q = deque()
        q.append(self.root)

        while q:
            curr = q.popleft()

            if curr.left is not None:
                q.append(curr.left)
            else:
                curr.left = Node(data)
                return self.root

            if curr.right is not None:
                q.append(curr.right)
            else:
                curr.right = Node(data)
                return self.root

    def in_order(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result 
    
    def _in_order_recursive(self, root, result):
        if root != None:
            self._in_order_recursive(root.left, result)
            result.append(root.key)
            self._in_order_recursive(root.right, result)
            return result 
    
    def pre_order(self):
        result = []
        self._pre_order_recursive(self.root, result)
    
    def _pre_order_recursive(self, root, result):
        if root != None:
            result.append(root.key)
            self._pre_order_recursive(root.left, result)
            self._pre_order_recursive(root.right, result)
            return result 
    
    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)
    
    def _post_order_recursive(self, root, result):
        if root != None:
            result.append(root.key)
            self._post_order_recursive(root.left, result)
            self._post_order_recursive(root.right, result)
            return result 
    
    def get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def search(self, target):
        return self._search_recursive( self.root, target)
        
    def _search_recursive(self, node, target):
        if node is None:
            return False
        if node.key == target:
            return True
        
        res1 = self._search_recursive(node.left, target)
        if res1:
            return True
        
        res2 = self._search_recursive(node.right, target)
        if res2:
            return True  
              
    def delete_deepest(self, root, dnode):
        queue = [root]

        while queue:
            curr = queue.pop(0)

            if curr == dnode:
                curr = None
                del dnode
                return

            if curr.right:
            
                if curr.right == dnode:
                    curr.right = None
                    del dnode
                    return
                queue.append(curr.right)

            if curr.left:
            
                if curr.left == dnode:
                    curr.left = None
                    del dnode
                    return
                queue.append(curr.left)

def deletion(self, key):
    if self.root is None:
        return None
    if self.root.left is None and self.root.right is None:
        if self.root.data == key:
            return None
        else:
            return self.root

    queue = [self.root]
    curr = None
    keyNode = None
    while queue:
        curr = queue.pop(0)
        if curr.data == key:
            keyNode = curr

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)


    if keyNode is not None:
        x = curr.data
        keyNode.data = x
        self.delete_deepest(self.root, curr)

    return self.root

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None
        
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
    
    
    def search(self, target):
        return self._search_recursive(target, self.root)

    def _search_recursive(self, target, node):
        if node is None:
            return False
        if node.key == target:
            return True
        if target > node.key:
            return self._search_recursive(target, node.right)
        else:
            return self._search_recursive(target, node.left)
    
        
tree = BinarySearchTree()
for i in range(110):
    tree.insert(i)
print(tree.search(100))

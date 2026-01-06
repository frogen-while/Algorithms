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
    def __str__(self):
            if self.root is None:
                return "Empty Tree"
            return self._build_tree_string(self.root, 0, "Root: ")

    def _build_tree_string(self, node, level, prefix):
        res = " " * (level * 4) + prefix + str(node.key) + "\n"
        if node.left or node.right:
            if node.left:
                res += self._build_tree_string(node.left, level + 1, "L--- ")
            else:
                res += " " * ((level + 1) * 4) + "L--- None\n"
            if node.right:
                res += self._build_tree_string(node.right, level + 1, "R--- ")
            else:
                res += " " * ((level + 1) * 4) + "R--- None\n"
        return res

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return self.root
        q = deque()
        q.append(self.root)

        while q:
            curr = q.popleft()

            if curr.left is not None:
                q.append(curr.left)
            else:
                curr.left = Node(key)
                return self.root

            if curr.right is not None:
                q.append(curr.right)
            else:
                curr.right = Node(key)
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
        return result
    
    def _pre_order_recursive(self, root, result):
        if root != None:
            result.append(root.key)
            self._pre_order_recursive(root.left, result)
            self._pre_order_recursive(root.right, result)
            return result 
    
    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result
    
    def _post_order_recursive(self, root, result):
        if root != None:
            self._post_order_recursive(root.left, result)
            self._post_order_recursive(root.right, result)
            result.append(root.key)
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
              
    def _delete_deepest(self, root, dnode):
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

    def delete(self, key):
        if self.root is None:
            return None
        if self.root.left is None and self.root.right is None:
            if self.root.key == key:
                return None
            else:
                return self.root

        queue = [self.root]
        curr = None
        keyNode = None
        while queue:
            curr = queue.pop(0)
            if curr.key == key:
                keyNode = curr

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)


        if keyNode is not None:
            x = curr.key
            keyNode.key = x
            self._delete_deepest(self.root, curr)

        return self.root
    def display(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left or node.right:
                if node.left:
                    self.display(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.display(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return super().__str__()
        
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
    
        
    def delete(self, target):
        self.root = self._delete_recursion(self.root, target)

    def _delete_recursion(self, root, target):
        if root is None:
            return root
        if target < root.key:
            root.left = self._delete_recursion(root.left, target)
        elif target > root.key:
            root.right = self._delete_recursion(root.right, target)

        else:

            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete_recursion(root.right, temp.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _delete_deepest(self, root, dnode):
        raise NotImplementedError("BinarySearchTree deletion uses a different logic and doesn't need _delete_deepest")
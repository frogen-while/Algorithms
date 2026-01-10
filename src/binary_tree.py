from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.key)

class TernaryNode(Node):
    def __init__(self, key):
        self.key = [key] 
        self.left = None
        self.middle = None
        self.right = None

    def __str__(self):
        return super().__str__()

class BinaryTree:
    def __init__(self):
        self.root = None
    def __str__(self):
            if self.root is None:
                return "Empty Tree"
            return BinaryTree._build_tree_string(self.root, 0, "Root: ")

    @staticmethod
    def _build_tree_string(node, level, prefix):
        res = " " * (level * 4) + prefix + str(node.key) + "\n"
        if node.left or node.right:
            if node.left:
                res += BinaryTree._build_tree_string(node.left, level + 1, "L--- ")
            else:
                res += " " * ((level + 1) * 4) + "L--- None\n"
            if node.right:
                res += BinaryTree._build_tree_string(node.right, level + 1, "R--- ")
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
        BinaryTree._in_order_recursive(self.root, result)
        return result 
    
    @staticmethod
    def _in_order_recursive(root, result):
        if root != None:
            BinaryTree._in_order_recursive(root.left, result)
            result.append(root.key)
            BinaryTree._in_order_recursive(root.right, result)
            return result 
    
    def pre_order(self):
        result = []
        BinaryTree._pre_order_recursive(self.root, result)
        return result
    
    @staticmethod
    def _pre_order_recursive(root, result):
        if root != None:
            result.append(root.key)
            BinaryTree._pre_order_recursive(root.left, result)
            BinaryTree._pre_order_recursive(root.right, result)
            return result 
    
    def post_order(self):
        result = []
        BinaryTree._post_order_recursive(self.root, result)
        return result
    
    @staticmethod
    def _post_order_recursive(root, result):
        if root != None:
            BinaryTree._post_order_recursive(root.left, result)
            BinaryTree._post_order_recursive(root.right, result)
            result.append(root.key)
            return result 
    
    def get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def search(self, target):
        return BinaryTree._search_recursive(self.root, target)
    
    @staticmethod
    def _search_recursive(node, target):
        if node is None:
            return False
        if node.key == target:
            return True
        
        res1 = BinaryTree._search_recursive(node.left, target)
        if res1:
            return True
        
        res2 = BinaryTree._search_recursive(node.right, target)
        if res2:
            return True  
              
    @staticmethod
    def _delete_deepest(root, dnode):
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
            BinaryTree._delete_deepest(self.root, curr)

        return self.root
    
    def clear(self):
        order = self.post_order()
        for key in order:
            self.delete(key)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return super().__str__()
        
    def insert(self, key):
        self.root = BinarySearchTree._insert_recursive(self.root, key)

    @staticmethod
    def _insert_recursive(cur_node, key):
        if cur_node is None:
            return Node(key)
        else:
            if key < cur_node.key:
                cur_node.left = BinarySearchTree._insert_recursive(cur_node.left, key)
            else:
                cur_node.right = BinarySearchTree._insert_recursive(cur_node.right, key)
        return cur_node
    
    
    def search(self, target):
        return BinarySearchTree._search_recursive(target, self.root)

    @staticmethod
    def _search_recursive(target, node):
        if node is None:
            return False
        if node.key == target:
            return True
        if target > node.key:
            return BinarySearchTree._search_recursive(target, node.right)
        else:
            return BinarySearchTree._search_recursive(target, node.left)
    
        
    def delete(self, target):
        self.root = BinarySearchTree._delete_recursion(self.root, target)

    @staticmethod
    def _delete_recursion(root, target):
        if root is None:
            return root
        if target < root.key:
            root.left = BinarySearchTree._delete_recursion(root.left, target)
        elif target > root.key:
            root.right = BinarySearchTree._delete_recursion(root.right, target)

        else:

            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = BinarySearchTree._min_value_node(root.right)
            root.key = temp.key
            root.right = BinarySearchTree._delete_recursion(root.right, temp.key)

        return root

    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    @staticmethod
    def _delete_deepest(root, dnode):
        raise NotImplementedError("BinarySearchTree deletion uses a different logic and doesn't need _delete_deepest")
    

class TernarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def _is_full(node):
        return len(node.key) == 2


    def insert(self, value):
        if self.root is None:
            self.root = TernaryNode(value)
        else:
            TernarySearchTree._insert_recursive(self.root, value)
        
        
    @staticmethod
    def _insert_recursive(cur_node, value):
        if value in cur_node.key:
            return

        if not TernarySearchTree._is_full(cur_node):
            cur_node.key.append(value)
            cur_node.key.sort()
            return 
        
        if value < cur_node.key[0]:
            if cur_node.left is None:
                cur_node.left = TernaryNode(value)
            else:
                TernarySearchTree._insert_recursive(cur_node.left, value)

        elif value > cur_node.key[1]:
            if cur_node.right is None:
                cur_node.right = TernaryNode(value)
            else:
                TernarySearchTree._insert_recursive(cur_node.right, value)

        else:
            if cur_node.middle is None:
                cur_node.middle = TernaryNode(value)
            else:
                TernarySearchTree._insert_recursive(cur_node.middle, value)
    
    
    def delete(self, value):
        self.root = TernarySearchTree._delete_recursive(self.root, value)

    @staticmethod
    def _delete_recursive(node, value):
        if node is None:
            return None

        if value < node.key[0]:
            node.left = TernarySearchTree._delete_recursive(node.left, value)
            return node
        
        if len(node.key) == 2 and value > node.key[1]:
            node.right = TernarySearchTree._delete_recursive(node.right, value)
            return node
            
        if len(node.key) == 2 and node.key[0] < value < node.key[1]:
            node.middle = TernarySearchTree._delete_recursive(node.middle, value)
            return node
        
        if len(node.key) == 1 and value > node.key[0]:
             node.middle = TernarySearchTree._delete_recursive(node.middle, value)
             return node

        if node.left is None and node.middle is None and node.right is None:
            if value in node.key:
                node.key.remove(value)
            
            if len(node.key) == 0:
                return None
            return node

        if value == node.key[0]:

            if node.middle is not None:
                successor_val = TernarySearchTree._get_min_value(node.middle)
                node.key[0] = successor_val 
                node.middle = TernarySearchTree._delete_recursive(node.middle, successor_val)
            else:
                node = node.left 
        

        elif len(node.key) == 2 and value == node.key[1]:

            if node.right is not None:
                successor_val = TernarySearchTree._get_min_value(node.right)
                node.key[1] = successor_val 

                node.right = TernarySearchTree._delete_recursive(node.right, successor_val)
            else:

                 node.key.pop()
        if len(node.key) == 0:
            return None
            
        return node
    
    @staticmethod
    def _get_min_value(node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key[0]
    
    def search(self, target):
        return TernarySearchTree._search_recursive(target, self.root)

    @staticmethod
    def _search_recursive(target, node):
        if node is None:
            return False

        if target in node.key:
            return True
        
        if target < node.key[0]:
            return TernarySearchTree._search_recursive(target, node.left)
        
        if len(node.key) == 2 and target > node.key[1]:
            return TernarySearchTree._search_recursive(target, node.right)
    
        return TernarySearchTree._search_recursive(target, node.middle)

    def in_order(self):
        result = [] 
        TernarySearchTree._in_order_recursive(self.root, result)
        return result
    
    @staticmethod
    def _in_order_recursive(root, result):
        if root is None:
            return 
        
        TernarySearchTree._in_order_recursive(root.left, result)
        result.append(root.key[0])
        TernarySearchTree._in_order_recursive(root.middle, result)

        if len(root.key) == 2:
            result.append(root.key[1])
            TernarySearchTree._in_order_recursive(root.right, result)
    
    def pre_order(self):
        result = [] 
        TernarySearchTree._pre_order_recursive(self.root, result)
        return result

    @staticmethod
    def _pre_order_recursive(node, result):
        if node is None:
            return 
        
        result.extend(node.key)
        TernarySearchTree._pre_order_recursive(node.left, result)
        TernarySearchTree._pre_order_recursive(node.middle, result)

        if len(node.key) == 2:
            TernarySearchTree._pre_order_recursive(node.right, result)
    
    def post_order(self):
        result = [] 
        TernarySearchTree._post_order_recursive(self.root, result)
        return result

    @staticmethod
    def _post_order_recursive(node, result):
        if node is None:
            return
        
        TernarySearchTree._post_order_recursive(node.left, result)
        TernarySearchTree._post_order_recursive(node.middle, result)

        if len(node.key) == 2:
            TernarySearchTree._post_order_recursive(node.right, result)

        result.extend(node.key)

    def clear(self):
        order = self.post_order()
        for key in order:
            self.delete(key)
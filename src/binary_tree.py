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
    
    def clear(self):
        order = self.post_order()
        for key in order:
            self.delete(key)

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
    

class TernarySearchTree:
    def __init__(self):
        self.root = None

    def _is_full(self, node):
        return len(node.key) == 2


    def insert(self, value):
        if self.root is None:
            self.root = TernaryNode(value)
        else:
            self._insert_recursive(self.root, value)
        
        

    def _insert_recursive(self, cur_node, value):
        if value in cur_node.key:
            return

        if not self._is_full(cur_node):
            cur_node.key.append(value)
            cur_node.key.sort()
            return 
        
        if value < cur_node.key[0]:
            if cur_node.left is None:
                cur_node.left = TernaryNode(value)
            else:
                self._insert_recursive(cur_node.left, value)

        elif value > cur_node.key[1]:
            if cur_node.right is None:
                cur_node.right = TernaryNode(value)
            else:
                self._insert_recursive(cur_node.right, value)

        else:
            if cur_node.middle is None:
                cur_node.middle = TernaryNode(value)
            else:
                self._insert_recursive(cur_node.middle, value)
    
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.key[0]:
            node.left = self._delete_recursive(node.left, value)
            return node
        
        if len(node.key) == 2 and value > node.key[1]:
            node.right = self._delete_recursive(node.right, value)
            return node
            
        if len(node.key) == 2 and node.key[0] < value < node.key[1]:
            node.middle = self._delete_recursive(node.middle, value)
            return node
        
        if len(node.key) == 1 and value > node.key[0]:
             node.middle = self._delete_recursive(node.middle, value)
             return node

        if node.left is None and node.middle is None and node.right is None:
            if value in node.key:
                node.key.remove(value)
            
            if len(node.key) == 0:
                return None
            return node

        if value == node.key[0]:

            if node.middle is not None:
                successor_val = self._get_min_value(node.middle)
                node.key[0] = successor_val 
                node.middle = self._delete_recursive(node.middle, successor_val)
            else:
                node = node.left 
        

        elif len(node.key) == 2 and value == node.key[1]:

            if node.right is not None:
                successor_val = self._get_min_value(node.right)
                node.key[1] = successor_val 

                node.right = self._delete_recursive(node.right, successor_val)
            else:

                 node.key.pop()
        if len(node.key) == 0:
            return None
            
        return node
        
    def _get_min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key[0]
    
    def search(self, target):
        return self._search_recursive(target, self.root)

    def _search_recursive(self, target, node):
        if node is None:
            return False

        if target in node.key:
            return True
        
        if target < node.key[0]:
            return self._search_recursive(target, node.left)
        
        if len(node.key) == 2 and target > node.key[1]:
            return self._search_recursive(target, node.right)
    
        return self._search_recursive(target, node.middle)

    def in_order(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, root, result):
        if root is None:
            return 

        self._in_order_recursive(root.left, result)
        result.append(root.key[0])
        self._in_order_recursive(root.middle, result)

        if len(root.key) == 2:
            result.append(root.key[1])
            self._in_order_recursive(root.right, result)
        return result
    
    def pre_order(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result):
        if node is None:
            return 
        
        result.extend(node.key)
        self._pre_order_recursive(node.left, result)
        self._pre_order_recursive(node.middle, result)

        if len(node.key) == 2:
            self._pre_order_recursive(node.right, result)

        return result
        
    
    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result

    
    def _post_order_recursive(self, node, result):
        if node is None:
            return
        self._post_order_recursive(node.left, result)
        self._post_order_recursive(node.middle, result)

        if len(node.key) == 2:
            self._post_order_recursive(node.right, result)

        result.extend(node.key)

    def clear(self):
        order = self.post_order()
        for key in order:
            self.delete(key)

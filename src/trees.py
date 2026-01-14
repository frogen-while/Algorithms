from __future__ import annotations

import sys

sys.setrecursionlimit(50000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self):
        return str(self.key)


class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

    def __str__(self):
        return super().__str__()


class TernaryNode:
    def __init__(self, key):
        self.key = [key]
        self.left: TernaryNode | None = None
        self.middle: TernaryNode | None = None
        self.right: TernaryNode | None = None

    def __str__(self):
        return str(self.key)


class BinarySearchTree:

    def __init__(self):
        self.root: Node | None = None


    def insert(self, key) -> None:
        self.root = self._insert_recursive(self.root, key)

    @staticmethod
    def _insert_recursive(node: Node | None, key) -> Node:
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = BinarySearchTree._insert_recursive(node.left, key)
        else:
            node.right = BinarySearchTree._insert_recursive(node.right, key)
        return node

    def search(self, target) -> bool:
        return self._search_recursive(self.root, target)

    @staticmethod
    def _search_recursive(node: Node | None, target) -> bool:
        if node is None:
            return False
        if node.key == target:
            return True
        if target < node.key:
            return BinarySearchTree._search_recursive(node.left, target)
        return BinarySearchTree._search_recursive(node.right, target)

    def delete(self, key) -> None:
        self.root = self._delete_recursive(self.root, key)

    @staticmethod
    def _delete_recursive(node: Node | None, key) -> Node | None:
        if node is None:
            return None
        if key < node.key:
            node.left = BinarySearchTree._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = BinarySearchTree._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = BinarySearchTree._min_value_node(node.right)
            node.key = successor.key
            node.right = BinarySearchTree._delete_recursive(node.right, successor.key)
        return node

    @staticmethod
    def _min_value_node(node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order(self) -> list:
        result: list = []
        self._in_order_recursive(self.root, result)
        return result

    @staticmethod
    def _in_order_recursive(node: Node | None, result: list) -> None:
        if node is not None:
            BinarySearchTree._in_order_recursive(node.left, result)
            result.append(node.key)
            BinarySearchTree._in_order_recursive(node.right, result)

    def pre_order(self) -> list:
        result: list = []
        self._pre_order_recursive(self.root, result)
        return result

    @staticmethod
    def _pre_order_recursive(node: Node | None, result: list) -> None:
        if node is not None:
            result.append(node.key)
            BinarySearchTree._pre_order_recursive(node.left, result)
            BinarySearchTree._pre_order_recursive(node.right, result)

    def post_order(self) -> list:
        result: list = []
        self._post_order_recursive(self.root, result)
        return result

    @staticmethod
    def _post_order_recursive(node: Node | None, result: list) -> None:
        if node is not None:
            BinarySearchTree._post_order_recursive(node.left, result)
            BinarySearchTree._post_order_recursive(node.right, result)
            result.append(node.key)


    def get_height(self, node: Node | None = None) -> int:
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def height(self) -> int:
        return self.get_height(self.root)

    def clear(self) -> None:
        self.root = None


class AVL(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.root: AVLNode | None = None

    @staticmethod
    def _height(node: AVLNode | None) -> int:
        return node.height if node else 0

    @staticmethod
    def _update_height(node: AVLNode) -> None:
        node.height = 1 + max(AVL._height(node.left), AVL._height(node.right))

    @staticmethod
    def _balance_factor(node: AVLNode | None) -> int:
        if node is None:
            return 0
        return AVL._height(node.left) - AVL._height(node.right)
    
    @staticmethod
    def _rotate_right(y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        AVL._update_height(y)
        AVL._update_height(x)
        return x

    @staticmethod
    def _rotate_left(x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        AVL._update_height(x)
        AVL._update_height(y)
        return y

    def insert(self, key) -> None:
        self.root = self._insert_avl(self.root, key)

    @staticmethod
    def _insert_avl(node: AVLNode | None, key) -> AVLNode:
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = AVL._insert_avl(node.left, key)
        else:
            node.right = AVL._insert_avl(node.right, key)

        AVL._update_height(node)
        balance = AVL._balance_factor(node)

        if balance > 1 and key < node.left.key:
            return AVL._rotate_right(node)

        if balance < -1 and key >= node.right.key:
            return AVL._rotate_left(node)

        if balance > 1 and key >= node.left.key:
            node.left = AVL._rotate_left(node.left)
            return AVL._rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = AVL._rotate_right(node.right)
            return AVL._rotate_left(node)

        return node


    def delete(self, key) -> None:
        self.root = self._delete_avl(self.root, key)

    @staticmethod
    def _delete_avl(node: AVLNode | None, key) -> AVLNode | None:
        if node is None:
            return None

        if key < node.key:
            node.left = AVL._delete_avl(node.left, key)
        elif key > node.key:
            node.right = AVL._delete_avl(node.right, key)
        else:

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
 
            successor = AVL._min_value_node_avl(node.right)
            node.key = successor.key
            node.right = AVL._delete_avl(node.right, successor.key)

        AVL._update_height(node)
        balance = AVL._balance_factor(node)

        if balance > 1 and AVL._balance_factor(node.left) >= 0:
            return AVL._rotate_right(node)
        if balance > 1 and AVL._balance_factor(node.left) < 0:
            node.left = AVL._rotate_left(node.left)
            return AVL._rotate_right(node)
        if balance < -1 and AVL._balance_factor(node.right) <= 0:
            return AVL._rotate_left(node)
        if balance < -1 and AVL._balance_factor(node.right) > 0:
            node.right = AVL._rotate_right(node.right)
            return AVL._rotate_left(node)

        return node

    @staticmethod
    def _min_value_node_avl(node: AVLNode) -> AVLNode:
        current = node
        while current.left is not None:
            current = current.left
        return current


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
            elif node.left is not None:
                predecessor_val = TernarySearchTree._get_max_value(node.left)
                node.key[0] = predecessor_val
                node.left = TernarySearchTree._delete_recursive(node.left, predecessor_val)
            elif len(node.key) == 2:
                node.key.pop(0)
                node.middle = node.right
                node.right = None
            else:
                return node.right

        elif len(node.key) == 2 and value == node.key[1]:
            if node.right is not None:
                successor_val = TernarySearchTree._get_min_value(node.right)
                node.key[1] = successor_val
                node.right = TernarySearchTree._delete_recursive(node.right, successor_val)
            else:
                node.key.pop()

        if node is None or len(node.key) == 0:
            return None

        return node

    @staticmethod
    def _get_min_value(node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key[0]

    @staticmethod
    def _get_max_value(node):
        current = node
        while current.right is not None:
            current = current.right
        return current.key[-1]

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
        self.root = None

    def get_height(self, node=None):
        if node is None and self.root is None:
            return 0
        if node is None:
            node = self.root
        left_h = self.get_height(node.left) if node.left else 0
        mid_h = self.get_height(node.middle) if node.middle else 0
        right_h = self.get_height(node.right) if node.right else 0
        return 1 + max(left_h, mid_h, right_h)

    def height(self):
        return self.get_height()

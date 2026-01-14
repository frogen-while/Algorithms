import unittest
from src.trees import AVL


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.avl = AVL()

    def test_empty_tree(self):
        self.assertIsNone(self.avl.root)
        self.assertEqual(self.avl.in_order(), [])
        self.assertFalse(self.avl.search(10))

    def test_insert_single(self):
        self.avl.insert(10)
        self.assertIsNotNone(self.avl.root)
        self.assertEqual(self.avl.root.key, 10)
        self.assertTrue(self.avl.search(10))

    def test_insert_multiple(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.avl.insert(v)

        self.assertEqual(self.avl.in_order(), sorted(values))
        for v in values:
            self.assertTrue(self.avl.search(v))

    def test_search_existing(self):
        values = [15, 10, 20, 8, 12, 17, 25]
        for v in values:
            self.avl.insert(v)

        for v in values:
            self.assertTrue(self.avl.search(v))

    def test_search_non_existing(self):
        values = [15, 10, 20]
        for v in values:
            self.avl.insert(v)

        self.assertFalse(self.avl.search(100))
        self.assertFalse(self.avl.search(-5))

    def test_left_left_rotation(self):
        for v in [30, 20, 10]:
            self.avl.insert(v)

        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.in_order(), [10, 20, 30])

    def test_right_right_rotation(self):
        for v in [10, 20, 30]:
            self.avl.insert(v)

        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.in_order(), [10, 20, 30])

    def test_left_right_rotation(self):
        for v in [30, 10, 20]:
            self.avl.insert(v)

        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.in_order(), [10, 20, 30])

    def test_right_left_rotation(self):
        for v in [10, 30, 20]:
            self.avl.insert(v)

        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.in_order(), [10, 20, 30])

    def test_balance_after_insertions(self):
        for v in range(1, 16):
            self.avl.insert(v)

        height = self.avl.height()
        self.assertLessEqual(height, 5)

    def test_delete_leaf(self):
        values = [50, 30, 70]
        for v in values:
            self.avl.insert(v)

        self.avl.delete(30)
        self.assertFalse(self.avl.search(30))
        self.assertTrue(self.avl.search(50))
        self.assertTrue(self.avl.search(70))

    def test_delete_node_with_children(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.avl.insert(v)

        self.avl.delete(30)
        self.assertFalse(self.avl.search(30))
        self.assertEqual(sorted([50, 70, 20, 40, 60, 80]), self.avl.in_order())

    def test_delete_root(self):
        values = [50, 30, 70]
        for v in values:
            self.avl.insert(v)

        self.avl.delete(50)
        self.assertFalse(self.avl.search(50))
        self.assertTrue(self.avl.search(30))
        self.assertTrue(self.avl.search(70))

    def test_delete_maintains_balance(self):
        for v in range(1, 16):
            self.avl.insert(v)
        for v in [5, 10, 15]:
            self.avl.delete(v)

        height = self.avl.height()
        self.assertLessEqual(height, 5)

    def test_delete_rebalance_left(self):
        for v in [20, 10, 30, 25, 35]:
            self.avl.insert(v)

        self.avl.delete(10)
        self.assertFalse(self.avl.search(10))


    def test_delete_rebalance_right(self):
        for v in [20, 10, 30, 5, 15]:
            self.avl.insert(v)

        self.avl.delete(30)
        self.assertFalse(self.avl.search(30))

    def test_in_order_traversal(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.avl.insert(v)

        self.assertEqual(self.avl.in_order(), sorted(values))

    def test_pre_order_traversal(self):
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.avl.insert(v)

        result = self.avl.pre_order()
        self.assertEqual(len(result), len(values))

    def test_post_order_traversal(self):
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.avl.insert(v)

        result = self.avl.post_order()
        self.assertEqual(len(result), len(values))

    def test_height_node(self):
        self.avl.insert(10)
        self.assertEqual(self.avl.root.height, 1)

        self.avl.insert(5)
        self.avl.insert(15)
        self.assertEqual(self.avl.root.height, 2)

    def test_clear(self):
        values = [50, 30, 70]
        for v in values:
            self.avl.insert(v)

        self.avl.clear()
        self.assertIsNone(self.avl.root)
        self.assertEqual(self.avl.in_order(), [])

    def test_negative_values(self):
        values = [-10, -5, 0, 5, 10]
        for v in values:
            self.avl.insert(v)

        self.assertEqual(self.avl.in_order(), values)
        for v in values:
            self.assertTrue(self.avl.search(v))

    def test_large_tree_balance(self):

        for v in range(1000):
            self.avl.insert(v)

        height = self.avl.height()
        self.assertLessEqual(height, 15)

    def test_stress_insert_delete(self):
        for v in range(100):
            self.avl.insert(v)

        for v in range(0, 100, 2):
            self.avl.delete(v)

        for v in range(1, 100, 2):
            self.assertTrue(self.avl.search(v))

        for v in range(0, 100, 2):
            self.assertFalse(self.avl.search(v))


if __name__ == "__main__":
    unittest.main()

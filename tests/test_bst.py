import unittest
from src.trees import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_empty_tree(self):
        self.assertIsNone(self.bst.root)
        self.assertEqual(self.bst.in_order(), [])
        self.assertEqual(self.bst.height(), 0)
        self.assertFalse(self.bst.search(10))

    def test_insert_single(self):
        self.bst.insert(10)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.key, 10)
        self.assertTrue(self.bst.search(10))

    def test_insert_multiple(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.bst.insert(v)

        self.assertEqual(self.bst.in_order(), sorted(values))
        for v in values:
            self.assertTrue(self.bst.search(v))

    def test_insert_duplicates(self):
        self.bst.insert(10)
        self.bst.insert(10)
        self.bst.insert(10)
        self.assertTrue(self.bst.search(10))

    def test_search_existing(self):
        values = [15, 10, 20, 8, 12, 17, 25]
        for v in values:
            self.bst.insert(v)

        for v in values:
            self.assertTrue(self.bst.search(v))

    def test_search_non_existing(self):
        values = [15, 10, 20]
        for v in values:
            self.bst.insert(v)

        self.assertFalse(self.bst.search(100))
        self.assertFalse(self.bst.search(-5))
        self.assertFalse(self.bst.search(0))

    def test_delete_leaf(self):
        values = [50, 30, 70]
        for v in values:
            self.bst.insert(v)

        self.bst.delete(30)
        self.assertFalse(self.bst.search(30))
        self.assertTrue(self.bst.search(50))
        self.assertTrue(self.bst.search(70))

    def test_delete_node_with_one_child(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)

        self.bst.delete(30)
        self.assertFalse(self.bst.search(30))
        self.assertTrue(self.bst.search(50))
        self.assertTrue(self.bst.search(20))

    def test_delete_node_with_two_children(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.bst.insert(v)

        self.bst.delete(30)
        self.assertFalse(self.bst.search(30))
        self.assertEqual(sorted([50, 70, 20, 40, 60, 80]), self.bst.in_order())

    def test_delete_root(self):
        values = [50, 30, 70]
        for v in values:
            self.bst.insert(v)

        self.bst.delete(50)
        self.assertFalse(self.bst.search(50))
        self.assertTrue(self.bst.search(30))
        self.assertTrue(self.bst.search(70))

    def test_delete_non_existing(self):
        self.bst.insert(10)
        self.bst.delete(100)
        self.assertTrue(self.bst.search(10))

    def test_in_order_traversal(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.bst.insert(v)

        self.assertEqual(self.bst.in_order(), [20, 30, 40, 50, 60, 70, 80])

    def test_pre_order_traversal(self):
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.bst.insert(v)

        result = self.bst.pre_order()
        self.assertEqual(result[0], 50)
        self.assertIn(30, result)
        self.assertIn(70, result)

    def test_post_order_traversal(self):
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.bst.insert(v)

        result = self.bst.post_order()
        self.assertEqual(result[-1], 50)

    def test_height_empty(self):
        self.assertEqual(self.bst.height(), 0)

    def test_height_single(self):
        self.bst.insert(10)
        self.assertEqual(self.bst.height(), 1)

    def test_height_balanced(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.bst.insert(v)
        self.assertEqual(self.bst.height(), 3)

    def test_height_linear(self):
        for v in [1, 2, 3, 4, 5]:
            self.bst.insert(v)
        self.assertEqual(self.bst.height(), 5)

    def test_clear(self):
        values = [50, 30, 70]
        for v in values:
            self.bst.insert(v)

        self.bst.clear()
        self.assertIsNone(self.bst.root)
        self.assertEqual(self.bst.in_order(), [])

    def test_str_empty(self):
        self.assertEqual(str(self.bst), "Empty Tree")

    def test_str_non_empty(self):
        self.bst.insert(10)
        self.assertIn("10", str(self.bst))

    def test_negative_values(self):
        values = [-10, -5, 0, 5, 10]
        for v in values:
            self.bst.insert(v)

        self.assertEqual(self.bst.in_order(), values)
        for v in values:
            self.assertTrue(self.bst.search(v))

    def test_large_tree(self):
        values = list(range(100))
        for v in values:
            self.bst.insert(v)

        self.assertEqual(self.bst.in_order(), values)
        self.assertTrue(self.bst.search(50))
        self.assertFalse(self.bst.search(200))


if __name__ == "__main__":
    unittest.main()

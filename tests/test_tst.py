import unittest
from src.trees import TernarySearchTree


class TestTernarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tst = TernarySearchTree()

    def test_empty_tree(self):
        self.assertIsNone(self.tst.root)
        self.assertEqual(self.tst.in_order(), [])
        self.assertFalse(self.tst.search(10))

    def test_insert_single(self):
        self.tst.insert(10)
        self.assertIsNotNone(self.tst.root)
        self.assertEqual(self.tst.root.key, [10])
        self.assertTrue(self.tst.search(10))

    def test_insert_two_values_same_node(self):
        self.tst.insert(10)
        self.tst.insert(20)

        self.assertEqual(self.tst.root.key, [10, 20])
        self.assertTrue(self.tst.search(10))
        self.assertTrue(self.tst.search(20))

    def test_insert_left_child(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.tst.insert(5)  
        self.assertEqual(self.tst.root.key, [10, 20])
        self.assertIsNotNone(self.tst.root.left)
        self.assertEqual(self.tst.root.left.key, [5])
        self.assertTrue(self.tst.search(5))

    def test_insert_right_child(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.tst.insert(30) 

        self.assertEqual(self.tst.root.key, [10, 20])
        self.assertIsNotNone(self.tst.root.right)
        self.assertEqual(self.tst.root.right.key, [30])
        self.assertTrue(self.tst.search(30))

    def test_insert_middle_child(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.tst.insert(15) 

        self.assertEqual(self.tst.root.key, [10, 20])
        self.assertIsNotNone(self.tst.root.middle)
        self.assertEqual(self.tst.root.middle.key, [15])
        self.assertTrue(self.tst.search(15))

    def test_insert_duplicate(self):
        self.tst.insert(10)
        self.tst.insert(10)

        self.assertEqual(self.tst.root.key, [10])

    def test_insert_multiple(self):
        values = [50, 30, 70, 20, 40, 60, 80, 25, 35]
        for v in values:
            self.tst.insert(v)

        self.assertEqual(self.tst.in_order(), sorted(values))
        for v in values:
            self.assertTrue(self.tst.search(v))

    def test_search_existing(self):
        values = [15, 10, 20, 8, 12, 17, 25]
        for v in values:
            self.tst.insert(v)

        for v in values:
            self.assertTrue(self.tst.search(v))

    def test_search_non_existing(self):
        values = [15, 10, 20]
        for v in values:
            self.tst.insert(v)

        self.assertFalse(self.tst.search(100))
        self.assertFalse(self.tst.search(-5))
        self.assertFalse(self.tst.search(0))

    def test_delete_single_node(self):
        self.tst.insert(10)
        self.tst.delete(10)

        self.assertIsNone(self.tst.root)
        self.assertFalse(self.tst.search(10))

    def test_delete_one_from_full_node(self):
        self.tst.insert(10)
        self.tst.insert(20)

        self.tst.delete(10)
        self.assertFalse(self.tst.search(10))
        self.assertTrue(self.tst.search(20))

    def test_delete_leaf_node(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.tst.insert(5)

        self.tst.delete(5)
        self.assertFalse(self.tst.search(5))
        self.assertTrue(self.tst.search(10))
        self.assertTrue(self.tst.search(20))

    def test_delete_node_with_children(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.tst.insert(v)

        self.tst.delete(50)
        self.assertFalse(self.tst.search(50))
        remaining = [v for v in values if v != 50]
        for v in remaining:
            self.assertTrue(self.tst.search(v))

    def test_delete_non_existing(self):
        self.tst.insert(10)
        self.tst.delete(100)
        self.assertTrue(self.tst.search(10))

    def test_in_order_traversal(self):
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.tst.insert(v)

        self.assertEqual(self.tst.in_order(), sorted(values))

    def test_in_order_empty(self):
        self.assertEqual(self.tst.in_order(), [])

    def test_pre_order_traversal(self):
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.tst.insert(v)

        result = self.tst.pre_order()
        self.assertEqual(len(result), len(values))
        self.assertIn(50, result)
        self.assertIn(30, result)

    def test_post_order_traversal(self):
        values = [50, 30, 70, 20, 40]
        for v in values:
            self.tst.insert(v)

        result = self.tst.post_order()
        self.assertEqual(len(result), len(values))

    def test_height_empty(self):
        self.assertEqual(self.tst.height(), 0)

    def test_height_single_node(self):
        self.tst.insert(10)
        self.assertEqual(self.tst.height(), 1)

    def test_height_two_values_same_node(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.assertEqual(self.tst.height(), 1)

    def test_height_with_children(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.tst.insert(5)
        self.tst.insert(25)

        self.assertEqual(self.tst.height(), 2)

    def test_clear(self):
        values = [50, 30, 70]
        for v in values:
            self.tst.insert(v)

        self.tst.clear()
        self.assertIsNone(self.tst.root)
        self.assertEqual(self.tst.in_order(), [])

    def test_negative_values(self):
        values = [-10, -5, 0, 5, 10]
        for v in values:
            self.tst.insert(v)

        self.assertEqual(self.tst.in_order(), values)
        for v in values:
            self.assertTrue(self.tst.search(v))

    def test_large_tree(self):
        values = list(range(100))
        for v in values:
            self.tst.insert(v)

        self.assertEqual(self.tst.in_order(), values)
        self.assertTrue(self.tst.search(50))
        self.assertFalse(self.tst.search(200))

    def test_delete_first_key_with_middle(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.tst.insert(15)

        self.tst.delete(10)
        self.assertFalse(self.tst.search(10))
        self.assertTrue(self.tst.search(15))
        self.assertTrue(self.tst.search(20))

    def test_delete_second_key_with_right(self):
        self.tst.insert(10)
        self.tst.insert(20)
        self.tst.insert(30)

        self.tst.delete(20)
        self.assertFalse(self.tst.search(20))
        self.assertTrue(self.tst.search(10))
        self.assertTrue(self.tst.search(30))

    def test_stress_insert_delete(self):
        for v in range(50):
            self.tst.insert(v)

        for v in range(0, 50, 2):
            self.tst.delete(v)

        for v in range(1, 50, 2):
            self.assertTrue(self.tst.search(v))

        for v in range(0, 50, 2):
            self.assertFalse(self.tst.search(v))


if __name__ == "__main__":
    unittest.main()

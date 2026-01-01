import unittest
from src import LinkedList as ll


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = ll.LinkedList()
        self.test_data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    def test_push_back(self):
        for el in self.test_data:
            self.linked_list.push_back(el)
        self.assertEqual(self.linked_list._size, len(self.test_data))
        for i, el in enumerate(self.test_data):
            self.assertEqual(self.linked_list.get(i), el)

    def test_push_front(self):
        for el in self.test_data:
            self.linked_list.push_front(el)
        self.assertEqual(self.linked_list._size, len(self.test_data))
        for i, el in enumerate(reversed(self.test_data)):
            self.assertEqual(self.linked_list.get(i), el)

    def test_pop_front(self):
        for el in self.test_data:
            self.linked_list.push_back(el)
        self.linked_list.pop_front()
        self.assertEqual(self.linked_list._size, len(self.test_data) - 1)
        self.assertEqual(self.linked_list.get(0), self.test_data[1])

    def test_pop_front_empty(self):
        with self.assertRaises(IndexError):
            self.linked_list.pop_front()

    def test_pop_front_single_element(self):
        self.linked_list.push_back(42)
        self.linked_list.pop_front()
        self.assertEqual(self.linked_list._size, 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_pop_back(self):
        for el in self.test_data:
            self.linked_list.push_back(el)
        self.linked_list.pop_back()
        self.assertEqual(self.linked_list._size, len(self.test_data) - 1)
        self.assertEqual(self.linked_list.get(self.linked_list._size - 1), self.test_data[-2])

    def test_pop_back_empty(self):
        with self.assertRaises(IndexError):
            self.linked_list.pop_back()

    def test_pop_back_single_element(self):
        self.linked_list.push_back(42)
        self.linked_list.pop_back()
        self.assertEqual(self.linked_list._size, 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_insert_middle(self):
        self.linked_list.push_back(1)
        self.linked_list.push_back(3)
        self.linked_list.insert(1, 2)
        self.assertEqual(self.linked_list._size, 3)
        self.assertEqual(self.linked_list.get(0), 1)
        self.assertEqual(self.linked_list.get(1), 2)
        self.assertEqual(self.linked_list.get(2), 3)

    def test_insert_front(self):
        self.linked_list.push_back(2)
        self.linked_list.insert(0, 1)
        self.assertEqual(self.linked_list.get(0), 1)
        self.assertEqual(self.linked_list.get(1), 2)

    def test_insert_back(self):
        self.linked_list.push_back(1)
        self.linked_list.insert(1, 2)
        self.assertEqual(self.linked_list.get(0), 1)
        self.assertEqual(self.linked_list.get(1), 2)

    def test_insert_invalid_index(self):
        self.linked_list.push_back(1)
        with self.assertRaises(IndexError):
            self.linked_list.insert(5, 99)
        with self.assertRaises(IndexError):
            self.linked_list.insert(-1, 99)

    def test_get(self):
        for el in self.test_data:
            self.linked_list.push_back(el)
        for i, el in enumerate(self.test_data):
            self.assertEqual(self.linked_list.get(i), el)

    def test_get_invalid_index(self):
        self.linked_list.push_back(1)
        with self.assertRaises(IndexError):
            self.linked_list.get(-1)
        with self.assertRaises(IndexError):
            self.linked_list.get(1)
        with self.assertRaises(IndexError):
            self.linked_list.get(100)

    def test_clear(self):
        for el in self.test_data:
            self.linked_list.push_back(el)
        self.linked_list.clear()
        self.assertEqual(self.linked_list._size, 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_clear_empty(self):
        self.linked_list.clear()
        self.assertEqual(self.linked_list._size, 0)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_erase_middle(self):
        self.linked_list.push_back(1)
        self.linked_list.push_back(2)
        self.linked_list.push_back(3)
        self.linked_list.erase(1)
        self.assertEqual(self.linked_list._size, 2)
        self.assertEqual(self.linked_list.get(0), 1)
        self.assertEqual(self.linked_list.get(1), 3)

    def test_erase_front(self):
        self.linked_list.push_back(1)
        self.linked_list.push_back(2)
        self.linked_list.erase(0)
        self.assertEqual(self.linked_list._size, 1)
        self.assertEqual(self.linked_list.get(0), 2)

    def test_erase_back(self):
        self.linked_list.push_back(1)
        self.linked_list.push_back(2)
        self.linked_list.erase(1)
        self.assertEqual(self.linked_list._size, 1)
        self.assertEqual(self.linked_list.get(0), 1)

    def test_erase_invalid_index(self):
        self.linked_list.push_back(1)
        with self.assertRaises(IndexError):
            self.linked_list.erase(-1)
        with self.assertRaises(IndexError):
            self.linked_list.erase(1)
        with self.assertRaises(IndexError):
            self.linked_list.erase(100)

    def test_push_back_scenarios(self):
        scenarios = [
            ("Powers of 2", [1, 2, 4, 8, 16]),
            ("Strings", ["hello", "world", "test"]),
            ("Mixed", [1, "two", 3.0, None]),
            ("Single Element", [42]),
            ("Empty", [])
        ]

        for name, data in scenarios:
            with self.subTest(case=name):
                linked_list = ll.LinkedList()
                for item in data:
                    linked_list.push_back(item)
                self.assertEqual(linked_list._size, len(data), f"Size mismatch in case '{name}'")
                cur_data = [linked_list.get(i) for i in range(linked_list._size)]
                self.assertEqual(cur_data, data, f"Content mismatch in case '{name}'")

    def test_get_invalid_indices(self):
        bad_indices = [-2, -1, 3, 4]

        for index in bad_indices:
            with self.subTest(bad_index=index):
                with self.assertRaises(IndexError, msg=f"get({index}) should fail"):
                    self.linked_list.get(index)


if __name__ == "__main__":
    unittest.main()

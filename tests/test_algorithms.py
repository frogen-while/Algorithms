import unittest
from src import algorithms as alg

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):

        self.test_cases = {
            "empty": [],
            "single": [1],
            "random": [3, 1, 4, 1, 5, 9, 2, 6, 5],
            "sorted": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "reversed": [9, 8, 7, 6, 5, 4, 3, 2, 1],
            "duplicates": [2, 2, 1, 1, 3, 3, 2, 1],
            "negative": [-3, 0, -1, 5, -2, 10],
            "large_range": [1000, 1, 500, 200, 0]
        }
        
        self.algorithms = {
            "Bubble Sort": alg.bubble_sort,
            "Insertion Sort": alg.insertion_sort,
            "Merge Sort": alg.merge_sort,
            "Quick Sort": alg.quick_sort,
            "Radix Sort": alg.radix_sort,
        }

    def test_all_sorts(self):
        for name, func in self.algorithms.items():
            for t_type, arr in self.test_cases.items():

                if name == "Radix Sort" and t_type == "negative":
                    continue

                with self.subTest(algorithm=name, case=t_type):
                    _arr = arr.copy()
                    expected = sorted(arr)

                    if name == "Quick Sort":
                        func(_arr, 0, len(_arr) - 1)
                    else:
                        result = func(_arr)
                        if result is not None:
                            _arr = result

                    self.assertEqual(_arr, expected, f"Failed: {name} on {t_type} case")

if __name__ == "__main__":
    unittest.main()




from src import algorithms as alg

test_cases = {
    "empty": [],
    "single": [1],
    "random": [3, 1, 4, 1, 5, 9, 2, 6, 5],
    "sorted": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "reversed": [9, 8, 7, 6, 5, 4, 3, 2, 1],
    "duplicates": [2, 2, 1, 1, 3, 3, 2, 1],
    "negative": [-3, 0, -1, 5, -2, 10],
    "large_range": [1000, 1, 500, 200, 0]
}
algorithms = {
    "Bubble Sort": alg.bubble_sort, 
    "Insertion Sort": alg.insertion_sort, 
    "Merge Sort": alg.merge_sort,
    "Quick Sort": alg.quick_sort,
    "Radix Sort":alg.radix_sort,
}


def test_all():
    for name, func in algorithms.items():
        print(f"Testing: {name}")
        for t_type, arr in test_cases.items():
            if name == "Radix Sort" and t_type == "negative":
                continue
            _arr = arr.copy()
            expected = sorted(arr)
            
            if name == "Quick Sort":
                func(_arr, 0, len(_arr) - 1)
            else:
                result = func(_arr)
                if result is not None:
                    _arr = result
            try:
                assert _arr == expected
                print(f"  ✅ {t_type}: OK")
            except AssertionError:
                print(f"  ❌ {t_type}: ERROR")
                print(f"     expected: {expected}")
                print(f"     received: {_arr}")

if __name__ == "__main__":
    test_all()




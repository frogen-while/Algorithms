import time

from src import algorithms as alg
from src import utils as ut

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_quick_sort.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/metrics_quick_sort.png"

SIZES = list(range(1000, 100001, 1000))
PIVOT_RANGE = range(1, 21)
ITERATIONS = 10

def compare_quick_sort(sizes: list) -> tuple:
    """Compare multi-pivot quicksort with different pivot counts."""
    results = []
    total = len(sizes)

    for step, size in enumerate(sizes, 1):
        print(f"[{step}/{total}] Processing size={size}...")
        row = {}
        for num_pivots in PIVOT_RANGE:
            durations = []
            for _ in range(ITERATIONS):
                arr = ut.generate_list(size)
                start = time.perf_counter()
                alg.multi_pivot_quicksort(arr, num_pivots)
                end = time.perf_counter()
                durations.append(end - start)
            row[f"Pivots: {num_pivots}"] = min(durations)
        results.append(row)

    print("Benchmark completed!")
    return sizes, results


if __name__ == "__main__":
    ut.save_metrics(PATH_TO_SAVE_TABLE, compare_quick_sort, sizes=SIZES)
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE)

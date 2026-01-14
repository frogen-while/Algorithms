import random
import time
from tqdm import tqdm 

from src import algorithms as alg
from src import utils as ut

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_algorithms.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/metrics_algorithms_plot.png"
PATH_TO_SAVE_TABLE_BIG = "outputs/tables/metrics_algorithms_big.csv"
PATH_TO_SAVE_PLOT_BIG = "outputs/plots/metrics_algorithms_big_plot.png"

ALGORITHMS = {
    "Bubble Sort": alg.bubble_sort,
    "Insertion Sort": alg.insertion_sort,
    "Merge Sort": alg.merge_sort,
    "Quick Sort": alg.quick_sort,
    "Radix Sort": alg.radix_sort,
}

SIZES = list(range(10, 1011, 100))
SIZES_BIG = list(range(1000, 10001, 1000))

ITERATIONS = 10

def compare_algorithms(
    listed_algs: dict,
    sizes: list[int],
    iterations: int = ITERATIONS,
) -> tuple:
    """Compare sorting algorithms across different input sizes."""
    results = []
    for size in tqdm(sizes):
        row = {}

        inputs = [ut.generate_list(size) for _ in range(iterations)]

        for name, func in listed_algs.items():
            durations = []
            for arr in inputs:
                start = time.perf_counter()
                func(arr)
                end = time.perf_counter()
                durations.append(end - start)
            row[name] = min(durations)

        results.append(row)
    return sizes, results


def build(
    iterations: int = ITERATIONS,
):
    ut.save_metrics(
        PATH_TO_SAVE_TABLE,
        compare_algorithms,
        listed_algs=ALGORITHMS,
        sizes=SIZES,
        iterations=iterations,
    )
    ut.save_metrics(
        PATH_TO_SAVE_TABLE_BIG,
        compare_algorithms,
        listed_algs=ALGORITHMS,
        sizes=SIZES_BIG,
        iterations=iterations,
    )
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE)
    ut.generate_plot(PATH_TO_SAVE_PLOT_BIG, PATH_TO_SAVE_TABLE_BIG)


if __name__ == "__main__":
    build()


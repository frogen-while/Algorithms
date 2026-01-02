from src import algorithms as alg
from src import utils as ut

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_algorithms.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/comparison_algorithms_plot.png"
PATH_TO_SAVE_TABLE_BIG = "outputs/tables/metrics_algorithms_big.csv"
PATH_TO_SAVE_PLOT_BIG = "outputs/plots/comparison_algorithms_plot_big.png"

ALGORITHMS = {
    "Bubble Sort": ut.timer(alg.bubble_sort),
    "Insertion Sort": ut.timer(alg.insertion_sort),
    "Merge Sort": ut.timer(alg.merge_sort),
    "Quick Sort": ut.timer(alg.quick_sort),
    "Radix Sort": ut.timer(alg.radix_sort),
}

SIZES = list(range(10, 1011, 100))
SIZES_BIG = list(range(1000, 10001, 1000))

ITERATIONS = 10


def compare_algorithms(listed_algs: dict, sizes: list) -> tuple:
    """Compare sorting algorithms across different input sizes."""
    results = []
    for size in sizes:
        row = {}
        for name, func in listed_algs.items():
            durations = []
            for _ in range(ITERATIONS):
                arr = ut.generate_list(size)
                _, duration = func(arr)
                durations.append(duration)
            row[name] = min(durations)
        results.append(row)
    return sizes, results


if __name__ == "__main__":
    ut.save_metrics(
        PATH_TO_SAVE_TABLE,
        compare_algorithms,
        listed_algs=ALGORITHMS,
        sizes=SIZES,
    )
    ut.save_metrics(
        PATH_TO_SAVE_TABLE_BIG,
        compare_algorithms,
        listed_algs=ALGORITHMS,
        sizes=SIZES_BIG,
    )
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE)
    ut.generate_plot(PATH_TO_SAVE_PLOT_BIG, PATH_TO_SAVE_TABLE_BIG)


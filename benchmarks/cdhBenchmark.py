import time

from src import algorithms as alg
from src import card_data_handler as cdh
from src import utils as ut

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_cdh.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/metrics_plot_cdh.png"

ALGORITHMS = {
    "Bubble Sort": alg.bubble_sort,
    "Insertion Sort": alg.insertion_sort,
    "Merge Sort": alg.merge_sort,
    "Quick Sort": alg.quick_sort,
    "Radix Sort": alg.radix_sort,
}

DATA_PATH = "data/carddump2.csv"
ITERATIONS = 10


def compare_card_data_handler(listed_algs: dict) -> tuple:
    """Compare sorting algorithms on credit card data."""
    size = 20000
    results = {}

    for name, func in listed_algs.items():
        durations = []
        for _ in range(ITERATIONS):
            start = time.perf_counter()
            cdh.sort_date_and_pin(
                DATA_PATH,
                savepath=None,
                needtosave=False,
                func=func,
            )
            end = time.perf_counter()
            durations.append(end - start)
        results[name] = min(durations)

    return size, results


if __name__ == "__main__":
    ut.save_metrics(
        PATH_TO_SAVE_TABLE,
        compare_card_data_handler,
        listed_algs=ALGORITHMS,
    )
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE, kind="bar")


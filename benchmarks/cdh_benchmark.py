import time
import pandas as pd
from tqdm import tqdm

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
SIZE = 20000
ITERATIONS = 10


def compare_card_data_handler(
    listed_algs: dict,
    iterations: int = ITERATIONS,
    data_path: str = DATA_PATH,
) -> tuple:
    """Compare sorting algorithms on credit card data."""

    full_df = pd.read_csv(data_path, dtype={"PIN": str, "Verification Code": str})
    subset = full_df.head(SIZE).reset_index(drop=True)

    row = {}
    for name, func in tqdm(listed_algs.items(), desc="Benchmark Card Data Handler"):
        durations = []
        for _ in range(iterations):
            start = time.perf_counter()
            cdh.sort_date_and_pin_df(subset, savepath=None, needtosave=False, func=func)
            end = time.perf_counter()
            durations.append(end - start)
        row[name] = min(durations)

    return SIZE, row


if __name__ == "__main__":
    ut.save_metrics(
        PATH_TO_SAVE_TABLE,
        compare_card_data_handler,
        listed_algs=ALGORITHMS,
        iterations=ITERATIONS,
        data_path=DATA_PATH,
    )
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE, kind="bar", xlabel="Size")


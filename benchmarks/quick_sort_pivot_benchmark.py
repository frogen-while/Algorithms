import random
import time
from tqdm import tqdm

from src import algorithms as alg
from src import utils as ut


PATH_TO_SAVE_TABLE = "outputs/tables/metrics_quick_sort.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/metrics_quick_sort.png"

SIZES = list(range(1000, 50001, 1000))
PIVOT_RANGE = range(1, 21)
ITERATIONS = 5
SEED = 42


def _make_list(size: int, seed: int) -> list[int]:
    rng = random.Random(seed)
    return [rng.randint(0, 5000) for _ in range(size)]

def compare_quick_sort(sizes: list[int], iterations: int = ITERATIONS, seed: int = SEED) -> tuple:
    results = []

    for size in tqdm(sizes, desc="Benchmark quicksort sizes"):
        row = {}
        
        base_arrays = [_make_list(size, seed + size + i) for i in range(iterations)]

        for num_pivots in PIVOT_RANGE:
            durations = []
            for i, base in enumerate(base_arrays):
                random.seed(seed + size + i * 1000 + num_pivots)
                start = time.perf_counter()
                alg.multi_pivot_quicksort(base, num_pivots)
                end = time.perf_counter()
                durations.append(end - start)
            row[f"Pivots: {num_pivots}"] = min(durations)
        results.append(row)
    return sizes, results


if __name__ == "__main__":
    ut.save_metrics(PATH_TO_SAVE_TABLE, compare_quick_sort, sizes=SIZES)
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE)

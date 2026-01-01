import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import utils as ut
from src import algorithms as alg

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_quick_sort.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/metrics_quick_sort.png"
sizes = [i for i in range(1000, 100001, 1000)]

def compare_quick_sort(sizes):
    results = []
    for size in sizes:
        row = {}
        for i in range(1, 21):
            durations = []
            for _ in range(10):
                arr = ut.generate_list(size)
                start = time.perf_counter()
                alg.multi_pivot_quicksort(arr, i)
                end = time.perf_counter()
                durations.append(end-start)
            row[f"Pivots: {i}"] = min(durations)
        results.append(row) 
    return sizes, results

if __name__ == "__main__":
    ut.save_metrics(PATH_TO_SAVE_TABLE, compare_quick_sort, sizes = sizes)
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE)
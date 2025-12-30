import sys
from pathlib import Path
root_path = str(Path(__file__).parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)

import pandas as pd
import matplotlib.pyplot as plt
from src import CardDataHandler as cdh
import random
from src import algorithms as alg
import time
import os


PATH_TO_SAVE_TABLE = "outputs/tables/metrics_algorithms.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/comparison_algorithms_plot.png"
PATH_TO_SAVE_TABLE_BIG = "outputs/tables/metrics_algorithms_big.csv"
PATH_TO_SAVE_PLOT_BIG = "outputs/plots/comparison_algorithms_plot_big.png"
PATH_TO_SAVE_TABLE_CDH = "outputs/tables/metrics_cdh.csv"
PATH_TO_SAVE_PLOT_CDH = "outputs/plots/metrics_plot_cdh.png"


def generate_list(size: int) -> list:
    return [random.randint(0, 5000) for _ in range(size)]

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end-start
    return wrapper

algorithms = {
    # "Bubble Sort": timer(alg.bubble_sort), 
    # "Insertion Sort":timer(alg.insertion_sort), 
    "Merge Sort": timer(alg.merge_sort),
    "Quick Sort": timer(alg.quick_sort),
    "Radix Sort":timer(alg.radix_sort),
}
algorithms_no_timer = {
    "Bubble Sort": alg.bubble_sort, 
    "Insertion Sort":alg.insertion_sort, 
    "Merge Sort":alg.merge_sort,
    "Quick Sort": alg.quick_sort,
    "Radix Sort":alg.radix_sort,
}
sizes = [n for n in range(10,1011,100)]
sizes_big =[n for n in range(1000, 10001, 1000)]

def compare_algorithms(listed_algs: dict, sizes):
    results = []
    for size in sizes:
        row = {}
        for name, func in listed_algs.items():
            durations = []
            for _ in range(10):
                arr = generate_list(size)
                if name == "Quick Sort":
                    _, duration = func(arr, 0, len(arr) - 1)
                else:
                    _, duration = func(arr)
                durations.append(duration)
            row[name] = min(durations)
        results.append(row)
    return sizes, results

def compare_card_data_handler(listed_algs: dict):
    size = 20000
    results = {}
    for name, func in listed_algs.items():
        durations = []
        for _ in range(10):
            start = time.perf_counter()
            cdh.sort_date_and_pin("data/carddump2.csv", savepath=None, needtosave=False, func=func)
            end = time.perf_counter()
            durations.append(end-start)
        results[name] = min(durations)

    return size, results

def compare_quick_sort(sizes):
    results = []
    for size in sizes:
        row = {}
        for i in range(1, min(20, min(sizes))):
            durations = []
            for _ in range(10):
                arr = generate_list(size)
                start = time.perf_counter()
                alg.multi_pivot_quicksort(arr, i)
                end = time.perf_counter()
                durations.append(end-start)
            row[f"Pivots: {i}"] = min(durations)
        results.append(row) 
    return sizes, results

    
def save_metrics(savepath, data_generator, **kwargs):
    os.makedirs(os.path.dirname(savepath), exist_ok=True)
    sizes, data = data_generator(**kwargs)
    index = [sizes] if isinstance(sizes, (int, float)) else sizes
    
    df = pd.DataFrame(data, index=index)
    df.to_excel(savepath, index_label="Size")
    print(f"Metrics saved to: {savepath}")

def generate_plot(savepath, pathtometrics, kind='line', title="Comparison", xlabel="Size", ylabel="Time (s)"):
    if not os.path.exists(pathtometrics):
        print(f"ERROR: FILE {pathtometrics} not found. Run save_metrics first")
        return

    df = pd.read_csv(pathtometrics, index_col='Size')
    plt.figure(figsize=(10, 6))
    
    if kind == 'bar':
        df.iloc[0].plot(kind='bar', ax=plt.gca(), color=plt.cm.Paired.colors)
        plt.xticks(rotation=45)
    else:
        df.plot(marker='o', ax=plt.gca())
        plt.grid(True, linestyle='--', alpha=0.7)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(savepath)
    plt.show()

save_metrics("outputs/tables/metrics_quick_sort.xlsx", compare_algorithms,listed_algs = algorithms,  sizes = sizes)

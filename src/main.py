import pandas as pd
import matplotlib.pyplot as plt
import card_data_handler as cdh
import random
import algorithms as alg
import time
import os

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_algorithms.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/comparison_algorithms_plot.png"
PATH_TO_SAVE_TABLE_BIG = "outputs/tables/metrics_algorithms_big.csv"
PATH_TO_SAVE_PLOT_BIG = "outputs/plots/comparison_algorithms_plot_big.png"
PATH_TO_SAVE_TABLE_CDH = "outputs/tables/metrics_cdh.csv"
PATH_TO_SAVE_PLOT_CDH = "outputs/plots/metrics_cdh.png"


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
    "Bubble Sort": timer(alg.bubble_sort), 
    "Insertion Sort":timer(alg.insertion_sort), 
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

    
def save_metrics(savepath, sizes):
    sizes, data = compare_card_data_handler(algorithms_no_timer) if savepath == "outputs/tables/metrics_cdh.csv" else compare_algorithms(algorithms, sizes) 
    df = pd.DataFrame(data, index=[sizes] if savepath == "outputs/tables/metrics_cdh.csv" else sizes)
    df.to_csv(savepath, index_label="Size")

def generate_plot(savepath, sizes, pathtometrics):
    if not os.path.exists(pathtometrics):
        save_metrics(pathtometrics, sizes) 
    

    df = pd.read_csv(pathtometrics, index_col='Size')
    if pathtometrics == "outputs/tables/metrics_cdh.csv":
        plt.figure(figsize=(10, 6))
    
        df.iloc[0].plot(kind='bar', ax=plt.gca(), color=['skyblue', 'orange', 'green', 'red', 'purple'])
        
        plt.title("Comparison of sorting algorithms (20k rows)")
        plt.xlabel("Algorithms")
        plt.ylabel("Time (seconds)")
        plt.xticks(rotation=45)

        plt.savefig(savepath)
        plt.show()
    else:
        df.plot(marker='o', ax=plt.gca())
        
        plt.title("Comparison of sorting algorithms")
        plt.xlabel("Array size (n)")
        plt.ylabel("Time (seconds)")
        plt.grid(True)
        
        plt.savefig(savepath)
        plt.show()


generate_plot(PATH_TO_SAVE_PLOT_CDH, None, PATH_TO_SAVE_TABLE_CDH)








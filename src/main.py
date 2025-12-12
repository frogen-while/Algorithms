import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import algorithms as alg
import statistics as st
import time
import os

PATH_TO_SAVE_TABLE = "outputs/tables/metrics.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/comparison_plot.png"


def generate_list(size: int) -> list:
    return [random.randint(0, 100) for _ in range(size)]

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

def compare_algorithms(listed_algs: dict):
    sizes = [10, 50, 100, 500, 1000, 3000]
    results = [{},{},{},{},{},{}]
    temp = []
    i = 0
    for size in sizes:
        for name, func in listed_algs.items():
            temp = []
            for _ in range(30):
                arr = generate_list(size)
                if name == "Quick Sort":
                    _, duration = func(arr, 0 , len(arr)-1)
                else:
                    _, duration = func(arr)    
                temp.append(duration)
            results[i][name] = round(st.mean(temp), 8)
        i+=1
            
    return sizes, results
    
def save_metrics(savepath):
    sizes, data = compare_algorithms(algorithms)
    df = pd.DataFrame(data, index=sizes)
    df.to_csv(savepath, index_label="Size")

def generate_plot(savepath):
    if not os.path.exists(PATH_TO_SAVE_TABLE):
        save_metrics(PATH_TO_SAVE_TABLE)
    

    df = pd.read_csv(PATH_TO_SAVE_TABLE, index_col='Size')
    
    os.makedirs(os.path.dirname(savepath), exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    df.plot(marker='o', ax=plt.gca())
    
    plt.title("Comparison of sorting algorithms")
    plt.xlabel("Array size (n)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    
    plt.savefig(savepath)
    plt.show()

generate_plot(PATH_TO_SAVE_PLOT)

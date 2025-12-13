import pandas as pd
import matplotlib.pyplot as plt
import random
import algorithms as alg
import statistics as st
import time
import os

PATH_TO_SAVE_TABLE = "outputs/tables/metrics.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/comparison_plot.png"
PATH_TO_SAVE_TABLE_BIG = "outputs/tables/metrics_big.csv"
PATH_TO_SAVE_PLOT_BIG = "outputs/plots/comparison_plot_big.png"


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
sizes = [n for n in range(10,1011,40)]
sizes_big =[n for n in range(1000, 10001, 200)]
def compare_algorithms(listed_algs: dict, sizes):
    results = [{} for _ in range(len(sizes))]
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
            results[i][name] = st.mean(temp)
        i+=1
            
    return sizes, results

    
def save_metrics(savepath, sizes):
    sizes, data = compare_algorithms(algorithms, sizes)
    df = pd.DataFrame(data, index=sizes)
    df.to_csv(savepath, index_label="Size")

def generate_plot(savepath, sizes, pathtometrics):
    if not os.path.exists(pathtometrics):
        save_metrics(pathtometrics, sizes)
    

    df = pd.read_csv(pathtometrics, index_col='Size')
    
    df.plot(marker='o', ax=plt.gca())
    
    plt.title("Comparison of sorting algorithms")
    plt.xlabel("Array size (n)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    
    plt.savefig(savepath)
    plt.show()









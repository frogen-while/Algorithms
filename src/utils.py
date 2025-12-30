import random
import time
import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_list(size: int) -> list:
    return [random.randint(0, 5000) for _ in range(size)]


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end-start
    return wrapper

def save_metrics(savepath, data_generator, **kwargs):
    os.makedirs(os.path.dirname(savepath), exist_ok=True)
    sizes, data = data_generator(**kwargs)
    index = [sizes] if isinstance(sizes, (int, float)) else sizes
    
    df = pd.DataFrame(data, index=index)
    df.to_csv(savepath, index_label="Size")
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


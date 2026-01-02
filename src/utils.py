import functools
import os
import random
import time
from typing import Callable, List, Tuple

import matplotlib.pyplot as plt
import pandas as pd


def generate_list(size: int) -> List[int]:
    """Generate a list of random integers."""
    return [random.randint(0, 5000) for _ in range(size)]


def timer(func: Callable) -> Callable:
    """Decorator to measure function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Tuple:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    return wrapper

def save_metrics(savepath: str, data_generator: Callable, **kwargs) -> None:
    """Save benchmark metrics to CSV file."""
    os.makedirs(os.path.dirname(savepath), exist_ok=True)
    sizes, data = data_generator(**kwargs)
    index = [sizes] if isinstance(sizes, (int, float)) else sizes

    df = pd.DataFrame(data, index=index)
    df.to_csv(savepath, index_label="Size")
    print(f"Metrics saved to: {savepath}")


def generate_plot(
    savepath: str,
    path_to_metrics: str,
    kind: str = 'line',
    title: str = "Comparison",
    xlabel: str = "Size",
    ylabel: str = "Time (s)"
) -> None:
    """Generate and save a plot from metrics CSV file."""
    if not os.path.exists(path_to_metrics):
        raise FileNotFoundError(
            f"Metrics file not found: {path_to_metrics}. Run save_metrics first."
        )

    df = pd.read_csv(path_to_metrics, index_col='Size')
    plt.figure(figsize=(10, 6))

    if kind == 'bar':
        df.iloc[0].plot(kind='bar', ax=plt.gca(), color=plt.cm.Paired.colors)
        plt.xticks(rotation=45)
    else:
        df.plot(marker='o', ax=plt.gca())
        plt.grid(True, linestyle='--', alpha=0.7)

    plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(savepath)
    plt.close()


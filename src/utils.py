from collections import deque
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

def get_bco_order(keys: List[int]) -> List[int]:
    """Rearange keys to best-case order"""
    
    sorted_keys = sorted(keys)
    result = []

    queue = deque([(0, len(sorted_keys) - 1)])
    
    while queue:
        left, right = queue.popleft()
        if left <= right:
            mid = (left + right) // 2
            result.append(sorted_keys[mid]) 

            queue.append((left, mid - 1))
            queue.append((mid + 1, right))
            
    return result

def get_bco_order_ternary(keys: List[int]) -> List[int]:
    sorted_keys = sorted(keys)
    result = []
    queue = [(0, len(sorted_keys) - 1)]
    head = 0
    while head < len(queue):
        lo, hi = queue[head]
        head += 1
        if lo > hi:
            continue

        length = hi - lo + 1

        if length == 1:
            result.append(sorted_keys[lo])
            continue

        if length == 2:
            result.append(sorted_keys[lo])
            result.append(sorted_keys[hi])
            continue

        third_1 = lo + length // 3
        third_2 = lo + 2 * length // 3

        if third_2 == third_1:
            third_2 += 1

        result.append(sorted_keys[third_1])
        result.append(sorted_keys[third_2])
        queue.append((lo, third_1 - 1))
        queue.append((third_1 + 1, third_2 - 1))
        queue.append((third_2 + 1, hi))
    return result
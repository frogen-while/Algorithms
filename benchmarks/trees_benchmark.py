import os
import random
import time
from tqdm import tqdm

from sortedcontainers import SortedSet

from src import trees as tree
from src import utils as ut


SIZES = [2**14 - 1]
ITERATIONS = 10
SEED = 42

PATH_TO_SAVE_TABLE_INSERT = "outputs/tables/metrics_trees_insert.csv"
PATH_TO_SAVE_TABLE_DELETE = "outputs/tables/metrics_trees_delete.csv"
PATH_TO_SAVE_TABLE_SEARCH = "outputs/tables/metrics_trees_search.csv"
PATH_TO_SAVE_TABLE_HEIGHT = "outputs/tables/metrics_trees_height.csv"

PATH_TO_SAVE_PLOT_INSERT = "outputs/plots/metrics_trees_insert.png"
PATH_TO_SAVE_PLOT_DELETE = "outputs/plots/metrics_trees_delete.png"
PATH_TO_SAVE_PLOT_SEARCH = "outputs/plots/metrics_trees_search.png"
PATH_TO_SAVE_PLOT_HEIGHT = "outputs/plots/metrics_trees_height.png"


def _tree_insert(obj, key) -> None:
    if hasattr(obj, "add"):
        obj.add(key)
    else:
        obj.insert(key)


def _tree_delete(obj, key) -> None:
    if hasattr(obj, "discard"):
        obj.discard(key)
    else:
        obj.delete(key)


def _tree_contains(obj, key) -> bool:
    if hasattr(obj, "__contains__"):
        return key in obj
    return obj.search(key)


def _tree_height(obj) -> int | None:
    if hasattr(obj, "height"):
        return obj.height()


def _fill_tree(obj, keys) -> None:
    for key in keys:
        _tree_insert(obj, key)


def _make_unique_keys(size: int, seed: int) -> list[int]:
    rng = random.Random(seed)
    population = max(size * 10, size + 1)
    return rng.sample(range(population), k=size)


def _build_configs(size: int, seed: int):
    random_keys = _make_unique_keys(size, seed)
    best_case_keys = ut.get_bco_order(random_keys)
    best_case_keys_ternary = ut.get_bco_order_ternary(random_keys)

    return [
        ("binary_search_tree_random", tree.BinarySearchTree, random_keys),
        ("ternary_tree_random", tree.TernarySearchTree, random_keys),
        ("avl_tree_random", tree.AVL, random_keys),
        ("sorted_set_random", SortedSet, random_keys),
        ("binary_search_tree_best-case", tree.BinarySearchTree, best_case_keys),
        ("ternary_tree_best-case", tree.TernarySearchTree, best_case_keys_ternary),
        ("avl_tree_best-case", tree.AVL, best_case_keys),
        ("sorted_set_best-case", SortedSet, best_case_keys)
    ]

def compare_insert(sizes: list[int], iterations: int = ITERATIONS, seed: int = SEED):
    results = []
    for size in sizes:
        configs = _build_configs(size, seed + size)
        row = {}
        for name, factory, keys in tqdm(configs, desc=f"Insert (size={size})"):
            durations = []
            for i in range(iterations):
                instance = factory()
                start = time.perf_counter()
                _fill_tree(instance, keys)
                end = time.perf_counter()
                durations.append(end - start)
            row[name] = min(durations)
        results.append(row)
    return sizes, results


def compare_delete(sizes: list[int], iterations: int = ITERATIONS, seed: int = SEED):
    results = []
    for size in sizes:
        configs = _build_configs(size, seed + size)
        row = {}
        for name, factory, keys in tqdm(configs, desc=f"Delete (size={size})"):
            durations = []
            for _i in range(iterations):
                instance = factory()
                _fill_tree(instance, keys)
                start = time.perf_counter()
                for key in keys:
                    _tree_delete(instance, key)
                end = time.perf_counter()
                durations.append(end - start)
            row[name] = min(durations)
        results.append(row)
    return sizes, results


def compare_search(sizes: list[int], iterations: int = ITERATIONS, seed: int = SEED):
    results = []
    for size in sizes:
        configs = _build_configs(size, seed + size)
        row = {}
        for name, factory, keys in tqdm(configs, desc=f"Search (size={size})"):
            instance = factory()
            _fill_tree(instance, keys)

            durations = []
            for _i in range(iterations):
                start = time.perf_counter()
                for key in keys:
                    _tree_contains(instance, key)
                end = time.perf_counter()
                durations.append(end - start)
            row[name] = min(durations)
        results.append(row)
    return sizes, results


def compare_height(sizes: list[int], seed: int = SEED):
    results = []
    for size in sizes:
        configs = _build_configs(size, seed + size)
        row = {}
        for name, factory, keys in tqdm(configs, desc=f"Height (size={size})"):
            if "sorted_set" in name:
                continue
            instance = factory()
            _fill_tree(instance, keys)
            row[name] = _tree_height(instance)
        results.append(row)
    return sizes, results


def build(
    sizes: list[int] = SIZES,
    iterations: int = ITERATIONS,
    seed: int = SEED,
):

    ut.save_metrics(PATH_TO_SAVE_TABLE_INSERT, compare_insert, sizes=sizes, iterations=iterations, seed=seed)
    ut.save_metrics(PATH_TO_SAVE_TABLE_DELETE, compare_delete, sizes=sizes, iterations=iterations, seed=seed)
    ut.save_metrics(PATH_TO_SAVE_TABLE_SEARCH, compare_search, sizes=sizes, iterations=iterations, seed=seed)
    ut.save_metrics(PATH_TO_SAVE_TABLE_HEIGHT, compare_height, sizes=sizes, seed=seed)

    plot_kind = "bar" if len(sizes) == 1 else "line"
    ut.generate_plot(PATH_TO_SAVE_PLOT_INSERT, PATH_TO_SAVE_TABLE_INSERT, kind=plot_kind, xlabel="Size")
    ut.generate_plot(PATH_TO_SAVE_PLOT_DELETE, PATH_TO_SAVE_TABLE_DELETE, kind=plot_kind, xlabel="Size")
    ut.generate_plot(PATH_TO_SAVE_PLOT_SEARCH, PATH_TO_SAVE_TABLE_SEARCH, kind=plot_kind, xlabel="Size")
    ut.generate_plot(PATH_TO_SAVE_PLOT_HEIGHT, PATH_TO_SAVE_TABLE_HEIGHT, kind="bar", xlabel="Size", ylabel="Height")

    return sizes

if __name__ == "__main__":
    build()

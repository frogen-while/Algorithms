from src import trees as tree
from src import utils as ut
from sortedcontainers import SortedSet 
import time
from tqdm import tqdm

def fill_tree(tree, keys):
    if hasattr(tree, 'add'):
        method = tree.add
    else:
        method = tree.insert

    for key in keys:
        method(key)

    return tree

def set_up():
    size = 2**16 - 1
    random_keys = ut.generate_list(size)
    best_case_keys = ut.get_bco_order(random_keys)

    configs = [
        ("binary_search_tree_random", tree.BinarySearchTree, random_keys),
        ("ternary_tree_random", tree.TernarySearchTree, random_keys),
        ("sorted_set_random", SortedSet, random_keys),
        ("binary_search_tree_best-case", tree.BinarySearchTree, best_case_keys),
        ("sorted_set_best-case", SortedSet, best_case_keys),
        ("ternary_tree_best-case", tree.TernarySearchTree, best_case_keys),
    ]
    return size, configs


def bench_insert(configs, size, iterations=10):
    result = {}
    
    for name, tree, keys in tqdm(configs, desc="Progress insert benchmark"):
        durations = []
        instance = tree()
        for _ in range(iterations):

            method = instance.add if hasattr(instance, 'add') else instance.insert
            
            start = time.perf_counter()
            for el in keys:
                method(el)
            end = time.perf_counter()
            durations.append(end - start)
            instance.clear()

        result[name] = min(durations)
        
    return size, result

def bench_deletion(configs,size, iterations=10):
    result = {}

    for name, tree, keys in tqdm(configs, desc="Progress delete benchmark"):
        durations = []
        instance = tree()
        for _ in range(iterations):
            fill_tree(instance, keys)
            if hasattr(instance, 'discard'):
                del_method = instance.discard
            else:
                del_method = instance.delete 

            start = time.perf_counter()
            for el in keys:
                del_method(el)
            end = time.perf_counter()
            durations.append(end - start)
            instance.clear()
            
        result[name] = min(durations)

    return size, result

def bench_search(configs, size, iterations=10):
    result = {}
    
    for name, tree, keys in tqdm(configs, desc="Progress search benchmark"):
        durations = []
    
        instance = tree()
        fill_tree(instance, keys)
        
        if hasattr(instance, '__contains__'):
            search_func = instance.__contains__
        else:
            search_func = instance.search


        for _ in range(iterations):
            start = time.perf_counter()
            for el in keys:
                search_func(el)
            end = time.perf_counter()
            durations.append(end - start)
            
        result[name] = min(durations)

        
    return size, result

def build(folder_to_save_metrics = "outputs/tables", folder_to_save_plots = "outputs/plots"):
    size, configs = set_up()
    print("Starting insertion benchmark")
    path_to_insertion = folder_to_save_metrics+"/metrics_trees_insert.csv"
    path_to_deletion = folder_to_save_metrics+"/metrics_trees_delete.csv"
    path_to_search = folder_to_save_metrics+"/metrics_trees_search.csv"
    path_to_insertion_plot = folder_to_save_plots+"/metrics_trees_insert.png"
    path_to_deletion_plot = folder_to_save_plots+"/metrics_trees_delete.png"
    path_to_search_plot = folder_to_save_plots+"/metrics_trees_search.png"
    ut.save_metrics(path_to_insertion, bench_insert, configs=configs, size = size)
    ut.save_metrics(path_to_deletion, bench_deletion, configs=configs, size = size)
    ut.save_metrics(path_to_search, bench_search, configs=configs, size = size)
    print("Metrics saved")
    ut.generate_plot(path_to_insertion_plot, path_to_insertion, kind="bar", xlabel="Insert")
    ut.generate_plot(path_to_deletion_plot, path_to_deletion, kind="bar", xlabel="Delete")
    ut.generate_plot(path_to_search_plot, path_to_search, kind="bar", xlabel="Search")
    return

if __name__ == "__main__":
    build()

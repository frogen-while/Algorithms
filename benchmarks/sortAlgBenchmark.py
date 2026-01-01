from src import utils as ut
from src import algorithms as alg

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_algorithms.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/comparison_algorithms_plot.png"
PATH_TO_SAVE_TABLE_BIG = "outputs/tables/metrics_algorithms_big.csv"
PATH_TO_SAVE_PLOT_BIG = "outputs/plots/comparison_algorithms_plot_big.png"

algorithms = {
    "Bubble Sort": ut.timer(alg.bubble_sort), 
    "Insertion Sort":ut.timer(alg.insertion_sort), 
    "Merge Sort": ut.timer(alg.merge_sort),
    "Quick Sort": ut.timer(alg.quick_sort),
    "Radix Sort":ut.timer(alg.radix_sort)
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
                arr = ut.generate_list(size)
                _, duration = func(arr)
                durations.append(duration)
            row[name] = min(durations)
        results.append(row)
    return sizes, results

if __name__ == "__main__":
    ut.save_metrics(PATH_TO_SAVE_TABLE, compare_algorithms, listed_algs = algorithms,  sizes = sizes)
    ut.save_metrics(PATH_TO_SAVE_TABLE_BIG, compare_algorithms, listed_algs = algorithms,  sizes = sizes_big)
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE)
    ut.generate_plot(PATH_TO_SAVE_PLOT_BIG, PATH_TO_SAVE_TABLE_BIG)


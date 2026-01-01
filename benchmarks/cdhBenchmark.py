import time
from src import utils as ut
from src import CardDataHandler as cdh
from src import algorithms as alg

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_cdh.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/metrics_plot_cdh.png"

algorithms = {
    # "Bubble Sort": alg.bubble_sort, 
    # "Insertion Sort": alg.insertion_sort, 
    "Merge Sort": alg.merge_sort,
    "Quick Sort": alg.quick_sort,
    "Radix Sort": alg.radix_sort
}

def compare_card_data_handler(listed_algs: dict):
    size = 20000
    results = {}
    for name, func in listed_algs.items():
        durations = []
        for _ in range(10):
            start = time.time()
            cdh.sort_date_and_pin("data/carddump2.csv", savepath=None, needtosave=False, func=func)
            duration = time.time() - start
            print(duration)
            durations.append(duration)
        results[name] = min(durations)

    return size, results

if __name__ == "__main__":
    ut.save_metrics(PATH_TO_SAVE_TABLE, compare_card_data_handler, listed_algs = algorithms)
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE, kind="bar")


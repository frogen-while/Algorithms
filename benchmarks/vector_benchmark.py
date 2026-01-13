import random
import time

from src import linked_list as ll
from src import utils as ut
from src import vector as v


SIZES = [100000]
ITERATIONS = 5
SEED = 42

PATH_TO_SAVE_TABLE = "outputs/tables/metrics_vector.csv"
PATH_TO_SAVE_PLOT = "outputs/plots/metrics_vector.png"


FACTORIES = {
    "Vector": v.Vector,
    "Linked list": ll.LinkedList,
    "List": list,
}


def _fill_object(obj, elements) -> None:
    if hasattr(obj, "push_back"):
        for el in elements:
            obj.push_back(el)
        return

    obj.extend(elements)


def _delete_at(obj, index: int) -> None:
    if hasattr(obj, "erase"):
        obj.erase(index)
        return
    obj.pop(index)


def _insert_at(obj, index: int, value) -> None:
    obj.insert(index, value)


def compare_vector_structures(
    sizes: list[int] = SIZES,
    iterations: int = ITERATIONS,
    seed: int = SEED,
    factories: dict = FACTORIES,
) -> tuple:
    results = []
    for size in sizes:
        rng = random.Random(seed + size)
        elements = [rng.randint(-5000, 5000) for _ in range(size)]
        delete_indices = [rng.randrange(size) for _ in range(iterations)]
        insert_indices = [rng.randrange(size) for _ in range(iterations)]

        row = {}
        for name, factory in factories.items():
            # append
            durations = []
            for _i in range(iterations):
                obj = factory()
                start = time.perf_counter()
                _fill_object(obj, elements)
                end = time.perf_counter()
                durations.append(end - start)
            row[f"{name} (append)"] = min(durations)

            # delete
            durations = []
            for index in delete_indices:
                obj = factory()
                _fill_object(obj, elements)
                start = time.perf_counter()
                _delete_at(obj, index)
                end = time.perf_counter()
                durations.append(end - start)
            row[f"{name} (delete)"] = min(durations)

            # insert
            durations = []
            for index in insert_indices:
                obj = factory()
                _fill_object(obj, elements)
                start = time.perf_counter()
                _insert_at(obj, index, 0)
                end = time.perf_counter()
                durations.append(end - start)
            row[f"{name} (insert)"] = min(durations)

        results.append(row)

    return sizes, results


def build(
    sizes: list[int] = SIZES,
    iterations: int = ITERATIONS,
    seed: int = SEED,
):
    ut.save_metrics(
        PATH_TO_SAVE_TABLE,
        compare_vector_structures,
        sizes=sizes,
        iterations=iterations,
        seed=seed,
    )
    plot_kind = "bar" if len(sizes) == 1 else "line"
    ut.generate_plot(PATH_TO_SAVE_PLOT, PATH_TO_SAVE_TABLE, kind=plot_kind, xlabel="Size")
    return sizes


if __name__ == "__main__":
    build()

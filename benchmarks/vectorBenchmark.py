import random
import time

from src import linked_list as ll
from src import utils as ut
from src import vector as v

SIZE = 1000000
ITERATIONS = 5
PATH = "outputs/tables/metrics_vector.csv"
PATH2 = "outputs/plots/metrics_vector.png"

def create_objects():
    return v.Vector(), ll.LinkedList(), []

def fill_object(obj, elements):
    if hasattr(obj, 'push_back'):
        for el in elements:
            obj.push_back(el)
    else:
        obj.extend(elements)

def bench_append(obj_factory, size):
    elements = [random.randint(-5000, 5000) for _ in range(size)]
    durations = []
    for _ in range(ITERATIONS):
        obj = obj_factory()
        start = time.perf_counter()
        if hasattr(obj, 'push_back'):
            for el in elements:
                obj.push_back(el)
        else:
            for el in elements:
                obj.append(el)
        end = time.perf_counter()
        durations.append(end - start)
    return min(durations)

def bench_delete(obj_factory, size):
    elements = [random.randint(-5000, 5000) for _ in range(size)]
    durations = []
    for _ in range(ITERATIONS):
        obj = obj_factory()
        fill_object(obj, elements)
        index = random.randint(0, size - 1)
        start = time.perf_counter()
        if hasattr(obj, 'erase'):
            obj.erase(index)
        else:
            obj.pop(index)
        end = time.perf_counter()
        durations.append(end - start)
    return min(durations)

def bench_insert(obj_factory, size):
    elements = [random.randint(-5000, 5000) for _ in range(size)]
    durations = []
    for _ in range(ITERATIONS):
        obj = obj_factory()
        fill_object(obj, elements)
        index = random.randint(0, size - 1)
        start = time.perf_counter()
        obj.insert(index, 0)
        end = time.perf_counter()
        durations.append(end - start)
    return min(durations)

def build():
    factories = {
        "Vector": v.Vector,
        "Linked list": ll.LinkedList,
        "List": list
    }
    
    result = {}
    for name, factory in factories.items():
        result[f"{name} (append)"] = [bench_append(factory, SIZE)]
        result[f"{name} (delete)"] = [bench_delete(factory, SIZE)]
        result[f"{name} (insert)"] = [bench_insert(factory, SIZE)]
    
    return SIZE, result

if __name__ == "__main__":
    ut.generate_plot(PATH2, PATH, kind="bar", xlabel=None)

import pandas as pd
import matplotlib.pyplot as plt
import csv
import random
from sorting_algthms import bubble_sort, merge_sort, quick_sort
import time

def generate_list(size: int,) -> list:
    return [random.randint(1, 100) for _ in range(size)]



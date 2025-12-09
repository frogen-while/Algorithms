import pandas as pd
import matplotlib.pyplot as plt
import csv
import random
import algorithms as alg
import time

def generate_list(size: int,) -> list:
    return [random.randint(1, 100) for _ in range(size)]


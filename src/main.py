import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import algorithms as alg
import statistics as st
import time

def generate_list(size: int) -> list:
    return [random.randint(0, 100) for _ in range(size)]

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end-start
    return wrapper


    

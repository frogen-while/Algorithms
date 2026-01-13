import random


def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(1, n):
        swapped = False
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(1,n):
        j = i - 1
        key = arr[i]
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def merge(left, right):
    sorted_array = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low
    for k in range(low, high):
        if arr[k] < pivot:
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def _quick_sort_recursive(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_recursive(arr, low, pi - 1)
        _quick_sort_recursive(arr, pi + 1, high)

def quick_sort(arr, low=None, high=None):
    arr = arr.copy()
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    _quick_sort_recursive(arr, low, high)
    return arr 

def radix_sort(arr):
    # Radix sort is for non-negative integers only
    n = len(arr)
    if n == 0:
        return arr
    
    arr = arr.copy()
    minval = min(arr)
    if minval < 0:
        raise ValueError("radix_sort does not support negative numbers")
    
    maxval = max(arr)
    exp = 1
    
    output = [0] * n
    
    while maxval // exp >= 1:
        count = [0] * 10
        
        for i in range(n):
            idx = (arr[i] // exp) % 10
            count[idx] += 1
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        for i in range(n - 1, -1, -1):
            idx = (arr[i] // exp) % 10
            count[idx] -= 1
            output[count[idx]] = arr[i]
        
        arr, output = output, arr
        
        exp *= 10
    
    return arr

def _select_pivots(arr, num_pivots):
    n = len(arr)
    if n <= num_pivots:
        return sorted(arr[:-1]) if n > 1 else []
    
    sample_size = min(num_pivots * 3, n)
    samples = sorted(random.sample(arr, sample_size))
    
    step = sample_size // (num_pivots + 1)
    pivots = [samples[(i + 1) * step] for i in range(num_pivots)]
    
    return pivots

def _binary_search_segment(pivots, x):

    left, right = 0, len(pivots)
    while left < right:
        mid = (left + right) // 2
        if x < pivots[mid]:
            right = mid
        else:
            left = mid + 1
    return left

def multi_pivot_quicksort(arr, num_pivots=2):

    n = len(arr)
    if n <= 1:
        return arr.copy() if n == 1 else []
    

    if n <= 16:
        result = arr.copy()
        for i in range(1, n):
            key = result[i]
            j = i - 1
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = key
        return result
    
    num_pivots = min(num_pivots, n - 1)
    
    pivots = _select_pivots(arr, num_pivots)
    actual_pivots = len(pivots)
    
    if actual_pivots == 0:
        return arr.copy()
    
    segments = [[] for _ in range(actual_pivots + 1)]
    pivot_counts = [0] * actual_pivots  
    
    for x in arr:
        seg_idx = _binary_search_segment(pivots, x)
        
        if seg_idx > 0 and x == pivots[seg_idx - 1]:
            pivot_counts[seg_idx - 1] += 1
        else:
            segments[seg_idx].append(x)
    
    result = []
    for i in range(actual_pivots):
        result.extend(multi_pivot_quicksort(segments[i], num_pivots))
        result.extend([pivots[i]] * pivot_counts[i])
    result.extend(multi_pivot_quicksort(segments[-1], num_pivots))
    
    return result






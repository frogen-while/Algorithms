
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
    
def multi_pivot_quicksort(arr, num_pivots=2):
    if len(arr) <= 1:
        return arr
    
    num_pivots = min(num_pivots, len(arr) - 1)
    
    pivots = sorted(arr[:num_pivots])
    
    segments = [[] for _ in range(num_pivots + 1)]
    
    for x in arr[num_pivots:]:
        placed = False
        for i in range(num_pivots):
            if x < pivots[i]:
                segments[i].append(x)
                placed = True
                break
        if not placed:
            segments[-1].append(x)
            
    result = []
    for i in range(num_pivots):
        result.extend(multi_pivot_quicksort(segments[i], num_pivots))
        result.append(pivots[i])
    result.extend(multi_pivot_quicksort(segments[-1], num_pivots))
    
    return result






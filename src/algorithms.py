
def bubble_sort(arr):
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
    sorted_array.extend(left[j:])
    return sorted_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for k in range(low, high):
        if arr[k] < pivot:
            arr[i], arr[k] = arr[k], arr[i]
            i+=1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_sort(arr, low, high):
    if low < high:
        
        pi = partition(arr, low, high)

        arr = quick_sort(arr, low, pi - 1)
        arr = quick_sort(arr, pi + 1, high)

    return arr 
# ONLY FOR RADIX!!! DOES NOT WORK INDEPENDENTLY!!!
def counting_sort(arr, exp):
    n = len(arr)
    ctnarr = [0] * 10
    ans = [0] * n 


    for i in range(n):
        index = arr[i] // exp
        ctnarr[index % 10] += 1
    
    for i in range(1, 10):
        ctnarr[i]+=ctnarr[i-1]

    i = n-1
    while i>=0:
        index = (arr[i]//exp)%10
        ans[ctnarr[index]-1] = arr[i]
        ctnarr[index]-=1
        i-=1

    return ans
def radix_sort(arr):
    maxval = max(arr)
    exp = 1
    while maxval / exp >=1:
        arr = counting_sort(arr, exp)
        exp*=10
    return arr
    






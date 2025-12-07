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




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


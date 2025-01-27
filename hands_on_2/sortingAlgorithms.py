''' 
Hands On 2:
1) The file, sortingAlgorithms.py" contains all 3 required sorting algorithms: Selection, Bubble and Insertion Sort.
2) random arrays with increases sizes are generated and saved with their corresponding run times to an external csv, "sortingRuntTimes.csv" file
3) The file, "sortingRuntTimes.csv",  will then be analyzed and visualised in another python noteboook further
'''

import timeit
import random
import pandas as pd


def bubbleSort(arr, length) :
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertionSort(arr, length) :
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selectionSort(arr, length) :
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def generateRandomArray(length) :
    return [random.randint(1, (length*2)) for _ in range(length)]



results_df = pd.DataFrame(columns=['ArraySize', 'BubbleSort (ms)', 'InsertionSort (ms)', 'SelectionSort (ms)'])
for arr_size in range(5, 10000):
    randomArray = generateRandomArray(arr_size)
    print("Iteration:", (arr_size-4))

    bubbleSortTime = timeit.timeit(lambda: bubbleSort(randomArray, arr_size), number=1)
    insertionSortTime = timeit.timeit(lambda: insertionSort(randomArray, arr_size), number=1)
    selectionSortTime = timeit.timeit(lambda: selectionSort(randomArray, arr_size), number=1)
    
    row = pd.DataFrame({'ArraySize': arr_size, 'BubbleSort (ms)': (bubbleSortTime*1000), 'InsertionSort (ms)': (insertionSortTime*1000), 'SelectionSort (ms)': (selectionSortTime*1000) }, index=[arr_size])
    row.to_csv("sortingAlgs_Benchmark_results.csv", mode="a", index=False, header=not pd.io.common.file_exists("sortingAlgs_Benchmark_results.csv"))



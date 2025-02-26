import random
import time
import openpyxl

def quicksort_non_random(arr, low, high):
    if low >= high:
        return
    pivot = arr[high]
    left, right = low, high
    
    while left < right:
        while arr[left] <= pivot and left < right:
            left += 1
        while arr[right] >= pivot and left < right:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
    
    arr[left], arr[high] = arr[high], arr[left]
    quicksort_non_random(arr, low, left - 1)
    quicksort_non_random(arr, left + 1, high)

def measure_time(arr):
    start_time = time.perf_counter_ns()
    quicksort_non_random(arr, 0, len(arr) - 1)
    end_time = time.perf_counter_ns()
    return end_time - start_time

def generate_best_case(arr):
    return sorted(arr)

def generate_worst_case(arr):
    return sorted(arr, reverse=True)

def main():
    file_name = "quick_sort_times.xlsx"
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Quick Sort Times"
    sheet.append(["n", "Best Time", "Average Time", "Worst Time"])
    
    for i in range(2, 100):
        n = i * 10
        arr = [random.randint(-10**6, 10**6) for _ in range(n)]
        
        best_case = generate_best_case(arr[:])
        average_case = arr[:]
        worst_case = generate_worst_case(arr[:])
        
        best_time = measure_time(best_case)
        average_time = measure_time(average_case)
        worst_time = measure_time(worst_case)
        
        sheet.append([n, best_time, average_time, worst_time])
    
    workbook.save(file_name)
    print("Excel file has been created successfully!")

if __name__ == "__main__":
    main()

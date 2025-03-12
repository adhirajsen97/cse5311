def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSelect(arr, low, high, i):
    if low < high:
        pivotIndex = partition(arr, low, high)
        if pivotIndex == i:
            return arr[pivotIndex]
        elif pivotIndex < i:
            return quickSelect(arr, pivotIndex + 1, high, i)
        else:
            return quickSelect(arr, low, pivotIndex - 1, i)
    return arr[low]

def main():
    arr = [9, 8, 7, 6]
    print("Array before sort:", arr)
    n = len(arr)
    order = 3  # Find the 3rd order statistic
    # quickSelect expects zero-indexed order so we pass order-1.
    ithOrderStatistic = quickSelect(arr, 0, n - 1, order - 1)
    print("Array after sort:", arr)
    print(f"The {order}th order statistic is: {ithOrderStatistic}")

if __name__ == '__main__':
    main()

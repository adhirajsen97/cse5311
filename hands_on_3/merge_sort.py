def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):

    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

test_array = [3, 6, 4, 4, 9, 2, 7, 5]
sorted_array = merge_sort(test_array)
print("Merge Sorted Array:", sorted_array)
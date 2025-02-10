import sys

def merge_sorted_arrays(array):
    n = sum(len(sub_array) for sub_array in array)  
    new_array = [0] * n  
    index = [0] * len(array)  
    current_index = 0

    while current_index < n:
        min_val = sys.maxsize  
        min_idx = -1

        for i in range(len(array)):
            if index[i] < len(array[i]) and array[i][index[i]] < min_val:
                min_val = array[i][index[i]]
                min_idx = i

        if min_idx != -1:
            new_array[current_index] = min_val
            index[min_idx] += 1
            current_index += 1

    return new_array


# Test cases
if __name__ == "__main__":
    array1 = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
    merged_array = merge_sorted_arrays(array1)
    print(merged_array)

    array2 = [[1, 3, 7], [2, 4, 8], [9, 10, 11]]
    merged_array = merge_sorted_arrays(array2)
    print(merged_array)

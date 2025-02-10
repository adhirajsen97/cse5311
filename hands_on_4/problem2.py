def remove_duplicates(arr):
    unique_list = [arr[0]]  

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  
            unique_list.append(arr[i])

    return unique_list


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    print(remove_duplicates(arr))
    
    arr2 = [2, 2, 2, 2, 2]
    print(remove_duplicates(arr2))

# Problem 0: 

## 1. Debug the code and "step into" the function for fib(5).

### Order of recursive calls: 

fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) -> fib(0) -> fib(1) -> fib(2) -> fib(1) -> fib(0) -> fib(3) -> fib(2) -> fib(1) -> fib(0) -> fib(1)


# Problem 1: Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.

## 1. Implement the solutions 

Code is implemented in `handson4/src/main/java/com/handson4/Problem1.java` 

## 2. Prove the time complexity of the algorithms

    The implemented code has the following steps:
    1. Iterating all the arrays to find total number of elements -> O(n) // n is total number of elements. 
    2. Merging loop scans all the three arrays to find the minimum element -> O(n)
    

    Overall Time complexity = O(n) + 0(n) = 0(n)

## 3. Comment on way's you could improve your implementation
    
    1. We can use binary heap data structure to efficient find the minimum element among the arrays, where insertion time in O(1) and Find-min is O(1).



# Problem 2: Given a sorted array array of size N, the task is to remove the duplicate elements from the array.

## 1. Implement the solutions 

Code is implemented in `handson4/src/main/java/com/handson4/Problem2.java`

## 2. Prove the time complexity of the algorithms

    The implemented code has the following steps:
    1. Iterating the sorted array -> O(n)
    2. Copying the elements to the array -> O(n)
    

    Overall Time complexity = O(n) + 0(n) = 0(n)

## 3. Comment on way's you could improve your implementation
    
    1. We can do the inplace removal of duplicate elements instead of using creating a new array, this will save us the space. We can utilize a two-pointer approach where one pointer traverses the array and another pointer points to the last unique element found.

    2. We can use HashSet to store unique elements while iterating through the array. Insertion time and lookup time for hashset is O(1) which can significantly improve the performance.
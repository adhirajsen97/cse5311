#include <iostream>
#include <vector>  // For using dynamic arrays (vectors)
using namespace std;

// Function to perform Bubble Sort
void bubbleSort(vector<int>& arr) {
    int n = arr.size();  // Get the size of the array
    bool swapped;

    for (int i = 0; i < n - 1; i++) {
        swapped = false;

        // Compare adjacent elements
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap if the current element is greater than the next element
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        // If no elements were swapped in the inner loop, the array is sorted
        if (!swapped)
            break;
    }
}

// Function to display the elements of the array
void printArray(const vector<int>& arr) {
    for (int val : arr) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};

    cout << "Original array: ";
    printArray(arr);

    bubbleSort(arr);

    cout << "Sorted array: ";
    printArray(arr);

    return 0;
}

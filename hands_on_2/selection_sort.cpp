#include <iostream>
#include <vector>
using namespace std;

void selectionSort(vector<int>& arr) {
    int size = arr.size();
    
    for (int i = 0; i < size - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        
        if (min_idx != i) {
            swap(arr[min_idx], arr[i]);
        }
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

    selectionSort(arr);

    cout << "Selection Sorted Array: ";
    printArray(arr);

    return 0;
}
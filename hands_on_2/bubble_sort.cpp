#include <iostream>
#include <vector>
#include <benchmark/benchmark.h>
using namespace std;

vector<int> arr = {64, 34, 25, 12, 22, 11, 90};

void bubbleSort(vector<int>& arr) {
    int size = arr.size();
    bool swapped;
    
    for (int i = 0; i < size - 1; i++) {
        swapped = false;
        
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
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

// Benchmark functions
static void BM_BubbleSort(benchmark::State& state) {
    for (auto _ : state) {
        
        cout << "Original array: ";
        printArray(arr);
        bubbleSort(arr);
    }
}

int main() {
    
    BENCHMARK(BM_BubbleSort)->RangeMultiplier(2)->Range(8, 8<<10);
    cout << "Bubble Sorted Array: ";
    printArray(arr);

    return 0;
}
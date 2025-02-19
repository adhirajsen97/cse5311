import math

class MinHeap:
    def __init__(self, capacity=10):
        self.array = []
        self.size = 0
        self.capacity = capacity
    
    def _get_parent(self, i):
        return (i - 1) >> 1
    
    def _get_left_child(self, i):
        return (i << 1) + 1
    
    def _get_right_child(self, i):
        return (i << 1) + 2
    
    def _swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.array[0]
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        root = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.size -= 1
        self._min_heapify(0)
        return root
    
    def insert(self, element):
        if self.size == self.capacity:
            self._resize_array(self.size * 2)
        self.array.append(element)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.array[self._get_parent(i)] > self.array[i]:
            self._swap(i, self._get_parent(i))
            i = self._get_parent(i)
    
    def build_min_heap(self, arr):
        if not arr:
            return
        self.array = arr[:]
        self.size = len(arr)
        for i in range((self.size // 2) - 1, -1, -1):
            self._min_heapify(i)
    
    def _min_heapify(self, i):
        smallest = i
        left_child = self._get_left_child(i)
        right_child = self._get_right_child(i)
        
        if left_child < self.size and self.array[left_child] < self.array[smallest]:
            smallest = left_child
        
        if right_child < self.size and self.array[right_child] < self.array[smallest]:
            smallest = right_child
        
        if smallest != i:
            self._swap(i, smallest)
            self._min_heapify(smallest)
    
    def _resize_array(self, new_size):
        self.capacity = new_size
    
    def print_min_heap(self):
        for i in range(self.size):
            print(self.array[i], end=" ")
            level = math.floor(math.log2(i + 1)) if i > 0 else 0
            print(" " * (level * 2), end="")
        print()  

if __name__ == "__main__":
    min_heap = MinHeap()
    
    min_heap.insert(6)
    min_heap.insert(8)
    min_heap.insert(2)
    min_heap.insert(3)
    min_heap.insert(3)
    min_heap.insert(0)
    min_heap.insert(15)
    min_heap.insert(50)
    
    print("Built heap:")
    min_heap.print_min_heap()
    
    print("Minimum element:", min_heap.peek())
    
    print("Popped element:", min_heap.pop())
    
    print("Heap after pop:")
    min_heap.print_min_heap()
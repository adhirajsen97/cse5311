import ctypes

class DynamicArray:
    def __init__(self):
        self.current_size = 0
        # Create a C-style array with capacity 1
        self.elements_array = (ctypes.c_int * 1)()
    
    def get_size(self):
        return self.current_size
    
    def append(self, element):
        if self.current_size == len(self.elements_array):
            self._increase_capacity(2 * len(self.elements_array))
        self.elements_array[self.current_size] = element
        self.current_size += 1
    
    def get_element_at(self, index):
        if index < 0 or index >= self.current_size:
            raise IndexError("Index is out of bounds")
        return self.elements_array[index]
    
    def remove_element(self, element):
        for i in range(self.current_size):
            if self.elements_array[i] == element:
                for j in range(i, self.current_size - 1):
                    self.elements_array[j] = self.elements_array[j + 1]
                self.current_size -= 1
                return
        raise ValueError("Element not found")
    
    def _increase_capacity(self, new_capacity):
        new_array = (ctypes.c_int * new_capacity)()
        for i in range(self.current_size):
            new_array[i] = self.elements_array[i]
        self.elements_array = new_array

# Main function to test the implementation
if __name__ == "__main__":
    my_array = DynamicArray()
    my_array.append(15)
    my_array.append(25)
    my_array.append(35)
    my_array.append(45)
    my_array.append(55)
    
    print(f"Array size: {my_array.get_size()}")
    print("Values in the Array: ", end="")
    for i in range(my_array.get_size()):
        print(f"{my_array.get_element_at(i)} ", end="")
    
    my_array.append(65)
    print("\nValues after adding: ", end="")
    for i in range(my_array.get_size()):
        print(f"{my_array.get_element_at(i)} ", end="")
    
    print(f"\nArray size after adding: {my_array.get_size()}")
    print(f"Value at index 2: {my_array.get_element_at(2)}")
    
    my_array.remove_element(25)
    print("Values after removing 25: ", end="")
    for i in range(my_array.get_size()):
        print(f"{my_array.get_element_at(i)} ", end="")
    
    print(f"\nArray size after removing: {my_array.get_size()}")
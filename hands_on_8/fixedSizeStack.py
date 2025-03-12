import random

class FixedSizeStack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.array = [None] * maxSize
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.maxSize - 1

    def push(self, item):
        if self.isFull():
            print("Overflow")
        else:
            self.top += 1
            self.array[self.top] = item

    def pop(self):
        if self.isEmpty():
            print("Underflow")
        else:
            self.array[self.top] = None
            self.top -= 1

    def firstElement(self):
        if self.isEmpty():
            print("Underflow")
            return None
        return self.array[0]

    def lastElement(self):
        if self.isEmpty():
            print("Underflow")
            return None
        return self.array[self.top]

    def elementAt(self, index):
        if self.isEmpty() or index < 0 or index > self.top:
            print("Underflow or Index out of bounds")
            return None
        return self.array[index]

    def numberOfElements(self):
        return self.top + 1

    def printStack(self):
        elements = ", ".join(str(self.array[i]) for i in range(self.top + 1))
        print("Stack: [" + elements + "]")
        print("Number of items:", self.numberOfElements())
        print("First item:", self.firstElement())
        print("Last item:", self.lastElement())

def main():
    stack = FixedSizeStack(10)
    
    print("Initial stack:")
    stack.printStack()
    
    print("\nAdd 5 numbers into the stack")
    for _ in range(5):
        stack.push(random.randint(0, 100))
    stack.printStack()
    
    print("\nAdd 2 numbers into the stack")
    for _ in range(2):
        stack.push(random.randint(0, 100))
    stack.printStack()
    
    print("\nItem at index 5:", stack.elementAt(5))
    
    print("\nRemove 5 items from the stack")
    for _ in range(5):
        stack.pop()
    stack.printStack()
    print("Stack number of items after pop:", stack.numberOfElements())

if __name__ == '__main__':
    main()

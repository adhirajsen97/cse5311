import random

class FixedSizeQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.array = [None] * maxSize
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return (self.head == (self.tail + 1) % self.maxSize) or (self.head == 0 and self.tail == self.maxSize - 1)

    def enqueue(self, item):
        if self.isFull():
            print("OVERFLOW!!!")
        else:
            self.array[self.tail] = item
            self.tail = (self.tail + 1) % self.maxSize

    def dequeue(self):
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return -1
        x = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.maxSize
        return x

    def headElement(self):
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        return self.array[self.head]

    def tailElement(self):
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        return self.array[(self.tail - 1 + self.maxSize) % self.maxSize]

    def elementAtIndexBehindHead(self, index):
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        elif ((self.head + index) % self.maxSize) >= self.tail:
            print("Index out of bounds")
            return None
        return self.array[(self.head + index) % self.maxSize]

    def numberOfElements(self):
        if self.head <= self.tail:
            return self.tail - self.head
        return self.maxSize - self.head + self.tail

    def printQueue(self):
        # Traverse the circular queue from head to tail.
        i = self.head
        elements = []
        while i != self.tail:
            elements.append(str(self.array[i]))
            i = (i + 1) % self.maxSize
            # Break if we loop all the way back (should not happen with correct logic)
            if i == self.head:
                break
        print("Queue: [" + ", ".join(elements) + "]")
        print("Number of items:", self.numberOfElements())
        print("Head:", self.head, ", Element:", self.headElement())
        print("Tail:", self.tail, ", Element:", self.tailElement())

def main():
    queue = FixedSizeQueue(10)
    
    print("Initial queue:")
    queue.printQueue()
    
    print("\nAdd 5 numbers into the queue")
    for _ in range(5):
        queue.enqueue(random.randint(0, 100))
    queue.printQueue()
    
    print("\nAdd 2 numbers into the queue")
    for _ in range(2):
        queue.enqueue(random.randint(0, 100))
    queue.printQueue()
    
    print("\nItem at index 5:", queue.elementAtIndexBehindHead(5))
    
    print("\nRemove 5 items from the queue")
    for _ in range(5):
        queue.dequeue()
    queue.printQueue()
    print("Queue number of items after dequeue:", queue.numberOfElements())

if __name__ == '__main__':
    main()

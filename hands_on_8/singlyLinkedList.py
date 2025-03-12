import random

class StaticSinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = [0] * capacity              # fixed array for integer values
        self.next = [i + 1 for i in range(capacity)]  # free list: each slot points to the next free slot
        self.next[-1] = -1                        # end of free list marker
        self.head = -1                            # -1 means the list is empty
        self.free = 0                             # pointer to the first free index
        self.size = 0

    def isEmpty(self):
        return self.head == -1

    def numberOfNodes(self):
        return self.size

    def insert(self, item):
        """Insert an integer at the end of the list.
           Prints an overflow message if the list is full."""
        if self.size == self.capacity:
            print("OVERFLOW!!!  Unable to insert the element. Linked List is full.")
            return
        # Allocate a new node from the free list.
        new_index = self.free
        self.free = self.next[new_index]  # update free pointer to next available slot
        self.values[new_index] = item
        self.next[new_index] = -1  # new node's next pointer is -1 (end of list)
        if self.head == -1:
            # List is empty: new node becomes the head.
            self.head = new_index
        else:
            # Traverse to the tail and attach the new node.
            current = self.head
            while self.next[current] != -1:
                current = self.next[current]
            self.next[current] = new_index
        self.size += 1

    def delete(self, node_index):
        """Delete the node at the given array index from the list.
           Mimics the Java behavior: if the node to delete is the head, clear the list."""
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return
        if self.head == node_index:
            # Deleting the head node clears the list.
            self.head = -1
            self.size = 0
            # Reinitialize the free list.
            self.free = 0
            for i in range(self.capacity):
                self.next[i] = i + 1 if i < self.capacity - 1 else -1
            return
        # Otherwise, find the node preceding the node to delete.
        prev = self.head
        while prev != -1 and self.next[prev] != node_index:
            prev = self.next[prev]
        if prev == -1:
            print("Node not found in the list.")
            return
        # Bypass the node to delete.
        self.next[prev] = self.next[node_index]
        # Add the deleted node index back to the free list.
        self.next[node_index] = self.free
        self.free = node_index
        self.size -= 1

    def headNode(self):
        """Return a representation of the head node, or print an underflow message."""
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        return self._get_node(self.head)

    def tailNode(self):
        """Return a representation of the tail node, or print an underflow message."""
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        current = self.head
        while self.next[current] != -1:
            current = self.next[current]
        return self._get_node(current)

    def nodeAtIndex(self, pos):
        """Return a representation of the node at the given position (0-indexed)."""
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        current = self.head
        count = 0
        while count < pos:
            if self.next[current] == -1:
                print("Index out of bounds")
                return None
            current = self.next[current]
            count += 1
        return self._get_node(current)

    def _get_node(self, index):
        """Helper to return a dictionary representing the node at a given array index."""
        return {"index": index, "value": self.values[index], "next": self.next[index]}

    def printLinkedList(self):
        """Prints all nodes in the list along with summary information."""
        if self.isEmpty():
            print("Linked List is empty")
        else:
            current = self.head
            nodes = []
            while current != -1:
                nodes.append(f"{self.values[current]} [index {current}]")
                current = self.next[current]
            print("Nodes:", " -> ".join(nodes))
        print("Size of LinkedList :", self.size)
        head_node = self.headNode()
        tail_node = self.tailNode()
        if head_node is not None:
            print("Head Element:", head_node["value"], "|", head_node)
        if tail_node is not None:
            print("Tail Element:", tail_node["value"], "|", tail_node)

def main():
    linkedList = StaticSinglyLinkedList(10)
    
    print("Add 5 items to the list")
    for i in range(5):
        # Insert random integers between 0 and 100.
        item = random.randint(0, 100)
        linkedList.insert(item)
    linkedList.printLinkedList()
    
    print("\nAdd 2 items to the List")
    for i in range(2):
        item = random.randint(0, 100)
        linkedList.insert(item)
    linkedList.printLinkedList()
    
    print("\nItem at index 5:", linkedList.nodeAtIndex(5))
    
    print("\nRemove the tail Element 5 times from the list")
    for i in range(5):
        tail = linkedList.tailNode()
        if tail is not None:
            # Delete the tail node by passing its array index.
            linkedList.delete(tail["index"])
    linkedList.printLinkedList()
    print("Linked List's number of items after pop:", linkedList.numberOfNodes())

if __name__ == '__main__':
    main()

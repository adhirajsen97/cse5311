import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        # This representation includes the value and a unique id (memory address)
        return f"<Node {self.value} at {hex(id(self))}>"

class SinglyLinkedList:
    def __init__(self, length):
        self.length = length  # maximum allowed nodes
        self.head = None

    def isEmpty(self):
        return self.head is None

    def numberOfNodes(self):
        if self.isEmpty():
            return 0
        count = 1
        node = self.head
        while node.next is not None:
            count += 1
            node = node.next
        return count

    def insert(self, node):
        if self.numberOfNodes() == self.length:
            print("OVERFLOW!!!  Unable to insert the element. Linked List is full.")
        else:
            if self.isEmpty():
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node

    def delete(self, node):
        if self.isEmpty():
            print("UNDERFLOW!!!")
        else:
            if self.head == node:
                # As in the Java code, deleting the head sets the list to empty.
                self.head = None
            else:
                previous = self.head
                # Loop until we find the node just before the one to delete.
                while previous.next != node:
                    previous = previous.next
                    if previous is None:
                        print("Node not found in the list.")
                        return
                previous.next = node.next

    def headNode(self):
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        return self.head

    def tailNode(self):
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        return current

    def nodeAtIndex(self, index):
        if self.isEmpty():
            print("UNDERFLOW!!!")
            return None
        current = self.head
        for i in range(index):
            if current.next is not None:
                current = current.next
            else:
                print("Index out of bounds")
                return None
        return current

    def printLinkedList(self):
        if not self.isEmpty():
            node = self.head
            # Print the starting node.
            print("Nodes:", node, end="")
            while node.next is not None:
                node = node.next
                print(" ->", node.value, f"[ {node} ]", end="")
            print()
        else:
            print("Linked List is empty")
        print("Size of LinkedList :", self.numberOfNodes())
        head_node = self.headNode()
        tail_node = self.tailNode()
        if head_node:
            print("Head Element:", head_node.value, "|", head_node)
        if tail_node:
            print("Tail Element:", tail_node.value, "|", tail_node)

def main():
    linkedList = SinglyLinkedList(10)

    print("Add 5 items to the list")
    for i in range(5):
        node = Node(random.randint(0, 100))
        linkedList.insert(node)
    linkedList.printLinkedList()

    print("\nAdd 2 items to the List")
    for i in range(2):
        node = Node(random.randint(0, 100))
        linkedList.insert(node)
    linkedList.printLinkedList()

    print("\nItem at index 5:", linkedList.nodeAtIndex(5))

    print("\nRemove the tail Element 5 times from the list")
    for i in range(5):
        tail = linkedList.tailNode()
        if tail is not None:
            linkedList.delete(tail)
    linkedList.printLinkedList()
    print("Linked List's number of items after pop:", linkedList.numberOfNodes())

if __name__ == '__main__':
    main()

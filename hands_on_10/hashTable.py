class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None  # pointer to next Node
        self.prev = None  # pointer to previous Node

class HashTable:
    def __init__(self, initial_capacity=10, load_factor=0.75, hash_function=None):
        self.initial_capacity = initial_capacity  
        self.load_factor_threshold = load_factor
        self.size = 0
        self.table = [None] * initial_capacity
        self.hash_function = hash_function if hash_function else self.division_hash

    def division_hash(self, key: int, table_size: int) -> int:
        return key % table_size

    def multiplication_hash(self, key: int, table_size: int, A=0.6180339887) -> int:
        frac = (key * A) % 1
        return int(table_size * frac)

    def get_index(self, key: int) -> int:
        table_size = len(self.table)
        return self.hash_function(key, table_size)

    def put(self, key: int, value: int):
        index = self.get_index(key)
        new_node = Node(key, value)
        # if no chain exists, start a new one
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1
        self.check_load_factor()

    def get(self, key: int) -> int:
        index = self.get_index(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int):
        index = self.get_index(key)
        current = self.table[index]
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    # node is at the head of the chain
                    self.table[index] = current.next
                if current.next:
                    current.next.prev = current.prev
                self.size -= 1
                self.check_load_factor()
                return
            current = current.next

    def check_load_factor(self):
        table_size = len(self.table)
        current_load = self.size / table_size
        if current_load >= self.load_factor_threshold:
            # Grow: double the table size.
            self._resize(table_size * 2)
        elif current_load <= 0.25 and table_size > self.initial_capacity:
            # Shrink: half the table size 
            new_capacity = max(self.initial_capacity, table_size // 2)
            self._resize(new_capacity)

    def _resize(self, new_capacity: int):
        old_table = self.table
        self.table = [None] * new_capacity
        old_size = self.size
        self.size = 0
        for head in old_table:
            current = head
            while current:
                next_node = current.next 
                current.next = None
                current.prev = None
                self._insert_node(current)
                current = next_node
        self.size = old_size

    def _insert_node(self, node: Node):
        index = self.get_index(node.key)
        if self.table[index] is None:
            self.table[index] = node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

    def print_table(self):
        for i, head in enumerate(self.table):
            print(f"Index {i}:", end=' ')
            current = head
            while current:
                print(f"({current.key}, {current.value})", end=' ')
                current = current.next
            print()

if __name__ == "__main__":
    ht = HashTable()
    ht.put(1, 90)
    ht.put(2, 70)
    ht.put(3, 40)
    ht.put(4, 90)
    ht.put(5, 30)

    print("Hash Table Size:", ht.size)
    ht.print_table()

    print("Value at Key 1:", ht.get(1))
    print("Value at Key 2:", ht.get(2))
    print("Value at Key 3:", ht.get(3))
    print("Value at Key 4:", ht.get(4))

    ht.remove(2)
    print("Hash Table Size after removal:", ht.size)
    ht.print_table()

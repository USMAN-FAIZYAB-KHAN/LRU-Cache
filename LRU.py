class Node:
    # Node class for a doubly linked list
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class DoublyLinkedList:
    # Doubly linked list class for managing cache nodes
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtStart(self, k, v):
        # Inserts a new node at the beginning of the linked list
        newNode = Node(k, v)
        newNode.right = self.head

        if self.head is not None:
            self.head.left = newNode

        self.size += 1
        self.head = newNode

        if self.tail is None:
            self.tail = newNode

        return newNode

    def deleteAtEnd(self):
        # Deletes the last node in the linked list
        prevNode = self.tail.left
        if prevNode is not None:
            prevNode.right = None
        else:
            self.head = None

        self.size -= 1
        key = self.tail.key
        self.tail = prevNode
        return key

    def makeItHead(self, node):
        # Moves a given node to the beginning of the linked list
        if node is not self.head:
            p = node.left
            r = node.right

            if p is not None:
                p.right = r

            if r is not None:
                r.left = p

            self.head.left = node
            node.right = self.head
            node.left = None

            if node is self.tail:
                self.tail = p

            self.head = node

    def traverse(self):
        # Prints the linked list elements
        print("{", end=" ")
        a = self.head
        while a.right is not None:
            print(f"{a.key}:{a.data},", end=" ")
            a = a.right
        print(f"{a.key}:{a.data}", end=" ")
        print("}")


class LRUCache:
    # LRU Cache implementation using a doubly linked list and a dictionary
    def __init__(self, capacity=None):
        self.cache = {}
        self.lst = DoublyLinkedList()
        self.capacity = capacity
        self.access = 0
        self.miss = 0

    def get(self, key: int) -> int:
        # Retrieves a value from the cache and updates its position
        self.access += 1
        node = self.cache.get(key)
        if node is not None:
            self.lst.makeItHead(node)
            return node.data
        else:
            self.miss += 1
            return -1

    def put(self, key: int, value: int) -> None:
        # Inserts a new key-value pair into the cache or updates an existing one
        n = self.cache.get(key)
        self.access += 1
        if n is not None:
            n.data = value
            self.lst.makeItHead(n)
        else:
            self.miss += 1
            if self.capacity == self.lst.size:
                k = self.lst.deleteAtEnd()
                if k is not None:
                    del self.cache[k]
            n = self.lst.insertAtStart(key, value)
            self.cache[key] = n


if __name__ == '__main__':
    # Sample usage of the LRUCache class
    print()
    lru = LRUCache(50)

    prime_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    access = 0 # counter for total number of accesses
    Total_miss = 0

    # Filling the cache with initial values
    for i in range(0, 50):
        Total_miss += 1
        access += 1
        lru.put(i, i)
    lru.lst.traverse()
    print(f"Miss Rate : {round((Total_miss/access)*100, 2)} %")
    print()

    # Accessing some elements to test cache hit/miss rates
    for i in range(1, 101, 2):
        i = lru.get(i)
        access += 1
        if i == -1:
            Total_miss += 1
    lru.lst.traverse()
    print(f"Miss Rate : {round((Total_miss/access)*100, 2)} %")
    print()

    # Accessing prime numbers to test cache hit/miss rates
    for i in range(0, len(prime_lst)):
        access += 1
        val = lru.get(prime_lst[i])

        if val == -1:
            lru.put(prime_lst[i], prime_lst[i])
            Total_miss += 1

    lru.lst.traverse()
    print(f"Final Miss Rate : {round((Total_miss/access)*100, 2)} %")
    print()

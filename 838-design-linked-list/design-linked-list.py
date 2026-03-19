class MyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = self.prev = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next
        return pointer.value

    def addAtHead(self, val: int) -> None:
        node = self.Node(val)

        if self.size == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = self.Node(val)

        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next

        node = self.Node(val)
        prev_node = pointer.prev

        prev_node.next = node
        node.prev = prev_node
        node.next = pointer
        pointer.prev = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next

        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
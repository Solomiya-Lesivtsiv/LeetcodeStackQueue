class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def is_empty(self):
        return self.head is None
    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def pop(self):
        if self.is_empty():
            return None
        new_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return new_value
    def peek(self):
        if self.is_empty():
            return None
        value = self.head.value
        return value
class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.add(x)
        for _ in range(self.queue.size - 1):
            old_val = self.queue.pop()
            self.queue.add(old_val)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
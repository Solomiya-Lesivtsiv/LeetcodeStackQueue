class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.is_empty():
            return None
        new_value = self.head.value
        self.head = self.head.next
        return new_value
    def peek(self):
        if self.is_empty():
            return None
        value = self.head.value
        return value
class MyQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()
    def push(self, x: int) -> None:
        return self.stack_in.push(x)

    def pop(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

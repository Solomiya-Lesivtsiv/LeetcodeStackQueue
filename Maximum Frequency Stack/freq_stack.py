from collections import deque, defaultdict

class FreqStack:
    def __init__(self):
        self.freq_map = defaultdict(int)
        self.groups = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        f = self.freq_map[val]
        if f > self.max_freq:
            self.max_freq = f
        self.groups[f].append(val)

    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()
        self.freq_map[val] -= 1
        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
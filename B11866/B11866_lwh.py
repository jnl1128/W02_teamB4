import sys
sys.stdin = open('B11866/input_lwh.txt', 'r')
input = sys.stdin.readline

class FixedQueue:
    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def is_empty(self):
        return self.no <= 0

    def enque(self, value):
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
    
    def dump(self):
        print('<', end='')
        for idx in range(self.no-1):
            print(f'{self.que[(idx + self.front) % self.capacity]}, ', end='')
        print(f'{self.que[(self.no-1 + self.front) % self.capacity]}>')


def dump(k):
    for _ in range(K-1):
        table.enque(table.deque())
    dumped.enque(table.deque())    

N, K = map(int, input().split())
table = FixedQueue(N)
dumped = FixedQueue(N)

for idx in range(1, N+1):
    table.enque(idx)

while True:
    if table.is_empty():
        dumped.dump()
        break
    dump(K)



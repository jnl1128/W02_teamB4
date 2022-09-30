# 카드2
import sys
input = sys.stdin.readline

class Queue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity:int=500000):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no>=self.capacity
    
    def __len__(self) -> int:
        return self.no

    def deque(self) -> int:
        if self.is_empty():
            raise Queue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
    
    def enque(self, value:int) -> None:
        if self.is_full():
            raise Queue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

def solution():
    N = int(input())
    q = Queue(N)
    for i in range(1, N+1):
        q.enque(i)
    
    while len(q) > 2:
        first = q.deque()
        second = q.deque()
        q.enque(second)
    if len(q) == 2:
        q.deque()
    return q.deque()

print(solution())
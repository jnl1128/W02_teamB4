# 최대 힙
import sys
input = sys.stdin.readline
print = sys.stdout.write

class PriorityQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity:int=100000):
        self.front = 0
        self.rear = 0
        self.no = 0
        self.que = [None]*capacity
        self.capacity = capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no>=self.capacity

    def deque(self) -> int:
        if self.is_empty():
            raise PriorityQueue.Empty
        x = self.que[self.front] #루트
        self.que[self.front], self.que[self.rear-1] = self.que[self.rear-1], self.que[self.front]
        parent = self.front 
        self.rear -= 1
        self.no -= 1
        while parent*2+1 < self.rear:
            childL = parent * 2 + 1
            childR = parent * 2 + 2
            child = 0
            if childR >= self.rear:
                child = childL
            else:
                if self.que[childL] > self.que[childR]:
                    child = childL
                else:
                    child = childR
            if self.que[parent] > self.que[child]:
                break
            else:
                self.que[parent], self.que[child] = self.que[child], self.que[parent]
            parent = child
        return x
        
            
    def enque(self, value:int) -> None:
        if self.is_full():
            raise PriorityQueue.Full

        self.que[self.rear] = value
        self.no += 1
        self.rear += 1
        if self.rear == self.capacity:
            self.rear = 0
        
        child = self.rear -1
        parent = (child -1)//2
        while parent >= self.front:
            if self.que[parent] < self.que[child]:
                self.que[parent], self.que[child] =  self.que[child], self.que[parent]
            child = parent
            parent = (child -1)//2
            


def solution():
    N = int(input())
    q = PriorityQueue(N)
    for _ in range(N):
        n = int(input())
        if n == 0:
            try:
                print(f'{q.deque()}\n')
            except PriorityQueue.Empty:
                print('0\n')
        else:
            q.enque(n)
        
solution()
# 큐2
import sys
input = sys.stdin.readline
print = sys.stdout.write
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
            
    def frontPeek(self) -> int:
        if self.is_empty():
            raise Queue.Empty
        else:
            return self.que[self.front]

    def backPeek(self) -> int:
        if self.is_empty():
            raise Queue.Empty
        else:
            return self.que[self.rear-1]


def solution():
    N = int(input())
    q = Queue(N)
    for _ in range(N):
        inputArr = list(input().rstrip().split(' '))
        if len(inputArr) == 2:
            q.enque(int(inputArr[1]))
        else:
            instruction = inputArr[0]
            if instruction == 'pop':
                try:
                    print(f'{q.deque()}\n')
                except:
                    print('-1\n')
            elif instruction == 'front':
                try:
                    print(f'{q.frontPeek()}\n')
                except:
                    print('-1\n')
            elif instruction == 'back':
                try:
                    print(f'{q.backPeek()}\n')
                except:
                    print('-1\n')
            elif instruction == 'empty':
                if q.is_empty():
                    print('1\n')
                else:
                    print('0\n')
            else:
                print(f'{len(q)}\n')
solution()
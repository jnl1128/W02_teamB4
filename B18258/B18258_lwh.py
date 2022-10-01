from re import S, X
import sys
sys.stdin = open('B18258/input_lwh.txt', 'r')
input = sys.stdin.readline

class FixedQueue:

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
    
    def __len__(self):
        return self.no

    def is_empty(self):
        return int(self.no <=0)

    def enque(self, value):
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
        
    def deque(self):
        if self.is_empty():
            return -1
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self):
        if self.is_empty():
            return -1
        return self.que[self.front]
    
    def peek_behind(self):
        if self.is_empty():
            return -1
        return self.que[self.rear-1]

def do(command):
    if command[:4] == 'push':
        value = command[5:]
        queue.enque(value)
    elif command == 'pop':
        print(queue.deque())
    elif command == 'size':
        print(queue.__len__())
    elif command == 'empty':
        print(queue.is_empty())
    elif command == 'front':
        print(queue.peek())
    elif command == 'back':
        print(queue.peek_behind())    

N = int(input())

queue = FixedQueue(N)

commands = [input().rstrip() for _ in range(N)]
for command in commands:
    do(command)

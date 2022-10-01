import sys
input = sys.stdin.readline

class FixedQueue:
    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
    
    def __len__(self):
        return self.no
    
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
        
def discard(cards):
    cards.deque()
    cards.enque(cards.deque())

N = int(input())
cards = FixedQueue(N)
for number in range(1,N+1):
    cards.enque(number)

while cards.__len__() > 1:
    discard(cards)

print(cards.deque())
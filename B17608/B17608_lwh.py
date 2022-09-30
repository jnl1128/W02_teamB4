import sys
sys.stdin = open('B17608/input_lwh.txt', 'r')
input = sys.stdin.readline

class Stack:
    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self):
        return self.ptr

    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def peek(self):
        return self.stk[self.ptr - 1]


    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]

    def show(self):
        for idx in range(self.ptr):
            print(self.stk[idx], end=' ')
        print('')

def how_many(sticks):
    count = sticks.__len__()
    veil = sticks.pop()
    for _ in range(sticks.__len__()):
        if sticks.peek() <= veil:
            count -= 1
            sticks.pop()
        elif sticks.peek() > veil:
            veil = sticks.pop()
    print(count)


N = int(input())
sticks = Stack(N)
for _ in range(N):
    sticks.push(int(input()))
how_many(sticks)


import sys
sys.stdin = open('B10773/input.txt', 'r')
input = sys.stdin.readline

class Stack:
    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1

    def sum(self):
        sum = 0
        for idx in range(self.ptr):
            sum += self.stk[idx]
        return sum

K = int(input())
integers = [int(input()) for _ in range(K)]
account = Stack(K)
for integer in integers:
    if integer == 0:
        account.pop()
    else:
        account.push(integer)

print(account.sum())


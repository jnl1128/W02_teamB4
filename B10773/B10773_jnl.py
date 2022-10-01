#제로
import sys
input = sys.stdin.readline
print = sys.stdout.write

class Stack:
    def __init__(self, capacity:int=100000):
        self.capacity = capacity
        self.stk = [None] * capacity
        self.ptr = 0

    def push(self, value:int) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> int:
        self.ptr -= 1
        return self.stk[self.ptr]

K = int(input())
stack = Stack(K)
total = 0
for _ in range(K):
    num = int(input())
    if num == 0:
        total -= stack.pop()
    else:
        stack.push(num)
        total += num
print(f'{total}')
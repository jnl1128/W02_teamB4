# 막대기
import sys
input = sys.stdin.readline
print = sys.stdout.write

class Stack:
    def __init__(self, capacity:int=100000):
        self.capacity = capacity
        self.stk = [None]*capacity
        self.ptr = 0

    def push(self, value:int) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> int:
        self.ptr -= 1
        return self.stk[self.ptr]

    def taller(self, value:int) -> int:
        cnt = 0
        for i in range(self.ptr-1,-1, -1):
            if self.stk[i] > value:
                cnt += 1
        return cnt

N = int(input())
stack = Stack(N)
for _ in range(N):
    stack.push(int(input()))
last = stack.pop()
print(f'{1+stack.taller(last)}')
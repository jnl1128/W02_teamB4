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

    def showingCnt(self) -> int:
        cnt = 0
        maxHeight = self.stk[self.ptr-1]
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] > maxHeight:
                cnt += 1
                maxHeight = self.stk[i]
        return cnt

N = int(input())
stack = Stack(N)
for _ in range(N):
    stack.push(int(input()))
print(f'{1+stack.showingCnt()}')
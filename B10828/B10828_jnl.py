# 스택
import sys
input = sys.stdin.readline
print = sys.stdout.write
class Stack:
    class Empty(Exception):
        pass
    def __init__(self, capacity: int = 10000):
        self.capacity = capacity
        self.stk = [None]*capacity
        self.ptr = 0
        
    def empty(self):
        return self.ptr == 0

    def push(self, value:int) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def top(self) -> int:
        if self.empty():
            raise Stack.Empty
        else:
            return self.stk[self.ptr-1]
    
    def size(self) -> int:
        return self.ptr

    def pop(self) -> int:
        if self.empty():
            raise Stack.Empty
        else:
            self.ptr -= 1
            return self.stk[self.ptr]

N = int(input())
arr = Stack(N)
for _ in range(N):
    inputArr = list(input().rstrip().split(' '))
    if len(inputArr) == 2:
        num = int(inputArr[1])
        arr.push(num)
    else:
        instruction = inputArr[0]
        if instruction == 'pop':
            try:
                print(f'{arr.pop()}\n')
            except Stack.Empty:
                print('-1\n')

        elif instruction == 'size':
            print(f'{arr.size()}\n')


        elif instruction == 'empty':
            if arr.empty():
                print('1\n')
            else:
                print('0\n')
        else:
            try:
                print(f'{arr.top()}\n')
            except Stack.Empty:
                print('-1\n')
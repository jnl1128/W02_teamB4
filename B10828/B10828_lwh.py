import sys
sys.stdin = open('B10828/input_lwh.txt', 'r')
input = sys.stdin.readline

class Stack:

    def __init__(self, capacity: int=256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self) -> int:
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0
    
    def push(self, value: int):
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self):
        if self.ptr <= 0:
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self):
        if self.ptr <= 0:
            return -1
        return self.stk[self.ptr-1]

def do_command(command):
    if command[:4] == 'push':
        value = command[5:]
        stack.push(value)

    elif command == 'pop':
        print(stack.pop())

    elif command == 'size':
        print(stack.__len__())

    elif command == 'empty':
        print(int(stack.is_empty()))

    elif command == 'top':
        print(stack.peek())
    return

N = int(input())
commands = [input().rstrip() for _ in range(N)]

stack = Stack(N)

for command in commands:
    do_command(command)

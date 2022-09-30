import sys
sys.stdin = open('B9012/input_lwh.txt', 'r')
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

    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def clear(self):
        self.ptr = 0

def is_VPS(stack):
    count_r = 0
    count_l = 0
    for _ in range(stack.__len__()):
        if stack.pop() == ')':
            count_r += 1
        else:
            count_l += 1
        if count_l > count_r :
            return 'NO'
    
    if count_l == count_r :
        return 'YES'
    else:
        return 'NO'

stack = Stack(50)

T = int(input())

for _ in range(T):
    for PS in input().rstrip():
        stack.push(PS)
    print(is_VPS(stack))
    stack.clear()


    
    
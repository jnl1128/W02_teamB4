import sys
sys.stdin = open('B2504/input_lwh.txt', 'r')
input = sys.stdin.readline

class Stack:
    def __init__(self, capacity):
        self.stk = [None]*capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):
        return self.ptr
    
    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1

    def show(self):
        for idx in range(self.ptr):
            print(self.stk[idx], end='')
        print()

def calculate(string):
    small = 0   # count ()
    big = 0     # count []
    
    local_sum = 0
    global global_sum
    
    for _ in range(string.__len__()):
        PS = string.pop()
        if PS == ')':
            small += 1
        elif PS == ']':
            big += 1
        elif PS == '(':
            small -= 1
            if small == 0 and  
        else:
            big -= 1
        if small == 0 and big > 0:
            local_sum *= 2
        elif small > 0 and big == 0:
            local_sum *= 3
        if small < 0 or big < 0 :
            print(0)
            return
    if small + big == 0:
        return 1

string = Stack(30)
global_sum = 0
for PS in input().rstrip():
    string.push(PS)

print(calculate(string))


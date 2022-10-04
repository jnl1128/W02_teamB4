import sys
sys.stdin = open('B2493/B2493_lwh.txt', 'r')
input = sys.stdin.readline

class FixedStack:

    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self):
        return self.ptr
    
    def is_empty(self):
        return self.ptr <= 0
    
    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self):
        if self.is_empty():
            return 0
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self):
        if self.is_empty():
            return 0
        return self.stk[self.ptr - 1]

    def clear(self):
        # self.ptr = 1
        # self.pop()
        self.ptr = 0

def radiate():
    highest = 0
    for idx, tower in enumerate(list(map(int, input().split()))):

        if tower > highest:
            highest = tower
            stack.clear()
            stack.push((idx+1, tower))
            print(0)
            continue
        
        while True:
            if stack.peek()[1] > tower:
                print(stack.peek()[0])
                stack.push((idx+1, tower))
                break
            elif stack.is_empty():
                print(0)
                break
            else: 
                stack.pop()
        

N =int(input())
stack = FixedStack(N)
radiate()

# 1. 왼쪽의 타워부터 stack에 push (count, height) tuple
# 2. highest 에 가장 높았던 값을 갱신.
#   2-1. highest 나오면 앞에있는거 clear 후 highest push
# 3.  

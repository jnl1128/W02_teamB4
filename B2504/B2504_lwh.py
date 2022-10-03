import sys
sys.stdin = open('2504.txt', 'r')
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
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            return -1
        return self.stk[self.ptr - 1]
    def peek2(self):
        if self.ptr >= 2:
            return self.stk[self.ptr -2]
        else:
            return True

# ( ( ) [ [ ] ] ) ( [ ] ) 
# =  2 * (2 + 3*3) + 2*3
# = 2*2 + 2*3*3 + 2*3
# : temp 에 곱해지는 수 (저장)

def calculate(string):
    ans = 0
    pairs = {'(':')', '[':']'}
    values = {'(':2, ')':2, '[':3, ']':3}
    temp = 1
    for idx in range(len(string)):
        if string[idx] in '([':
            stack.push(string[idx])
            temp *= values[string[idx]]
        elif string[idx] == ')':
            if stack.is_empty() or stack.peek() == '[':
                ans = 0
                break
            if string[idx-1] == '(':
                ans += temp
            stack.pop()
            temp //= values[string[idx]]
        else:
            if stack.is_empty() or stack.peek() == '(':
                ans = 0
                break
            if string[idx-1] == '[':
                ans += temp
            stack.pop()
            temp //= values[string[idx]]

    if stack.is_empty():
        print(ans)
    else:
        print(0)

string = input().rstrip()
stack = FixedStack(len(string))
calculate(string)
                


        


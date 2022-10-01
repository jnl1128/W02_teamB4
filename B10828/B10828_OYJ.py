import sys
sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
stack = [None]*n
ptr = 0 

# push X: 정수 X를 스택에 넣는 연산이다.
def push(data):
    global ptr
    global stack
    stack[ptr] = data
    ptr += 1
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    global ptr
    global stack
    if ptr == 0 :
        print(-1)
    else: 
        print(stack[ptr-1])
        del stack[ptr-1]

        ptr -= 1
# size: 스택에 들어있는 정수의 개수를 출력한다.
def size():
    global ptr
    global stack
    print(ptr)
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    global ptr
    global stack
    if ptr == 0 :
        print(1)
    else: 
        print(0)
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
def top():
    global ptr
    global stack
    if ptr == 0:
        print(-1)
    else :
        print(stack[ptr-1])

for i in range(n):
    instruction = sys.stdin.readline().rstrip()
    if instruction[:4] =='push':
        pushed_data = int(instruction[5:])
        push(pushed_data)
    elif instruction == 'pop':
        pop()
    elif instruction == 'size':
        size()
    elif instruction == 'empty':
        empty()
    elif instruction == 'top':
        top()


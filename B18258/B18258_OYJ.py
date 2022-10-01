import sys
sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
stack = [None]*n
front = 0 
rear = 0
no= 0 

# push X: 정수 X를 큐에 넣는 연산이다.
def push(data):
    global stack
    global front
    global rear
    global no
    stack[rear] = data
    if rear == n:
        rear = 0
    else:
        rear +=1
    no += 1
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    global stack
    global front
    global no
    if no ==0 :
        print(-1)
    else : 
        print(stack[front])
        stack[front] = None
        if front == n:
            front = 0
        else:
            front +=1
        no -=1
    
# size: 큐에 들어있는 정수의 개수를 출력한다.
def size():
    global no
    print(no)
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
def empty():
    global no
    if no == 0 :
        print(1)
    else: 
        print(0)
# 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def get_front():
    global stack
    global front
    global no
    if no == 0:
        print(-1)
    else :
        print(stack[front])
# 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def get_back():
    global stack
    global rear
    global no
    if no == 0:
        print(-1)
    else :
        print(stack[rear-1])

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
    elif instruction == 'front':
        get_front()
    elif instruction == 'back':
        get_back()


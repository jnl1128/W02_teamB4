from collections import deque
N, K = map(int, input().split(' '))
arr = list(map(int,list(input().rstrip())))

stack = deque([])
result = ''
for idx, num in enumerate(arr):
    pos = len(result)
    
    while stack and stack[-1] < num:
        stack.pop()
    stack.append(num)
    
    if idx == (N-(N-K)+pos):
        # 선택의 순간
        result += str(stack.popleft())
print(f'{result}')


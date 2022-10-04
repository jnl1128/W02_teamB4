from collections import deque
N, K = map(int, input().split(' '))
arr = list(map(int,list(input().rstrip())))

stack = deque([])
result = ''
for idx, num in enumerate(arr):
    pos = len(result)
    
    while stack and stack[-1] < num:
        a = stack.pop()
        # print('기준: ', num, 'pop', a)
    stack.append(num)
    # print('stack:', stack)

    if idx == (N-(N-K)+pos):
        # print('선택의 순간', idx)
        result += str(stack.popleft())
        # result.append(str(stack.popleft()))
print(f'{result}')


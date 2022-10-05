# 히스토크램에서 가장 큰 직사각형
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

# 높이가 중요한게 아니라 넓이가 중요한 것
def solution(squares):
    result = 0
    stack = deque([[1, squares[0]]])
    for square in squares[1:]:
        # 바로 전꺼보다 작은게 들어왔으면
        if square < stack[-1][1]:
        
            flag = True
            for _ in range(len(stack)):
                s = stack.popleft()
                # 현재 들어온 것보다 큰것들은 곱셈해주고 
                if s[1] > square:
                    result = max(result, s[1]*s[0])

                # 현재 들어온 것보다 작은 것들은 가로 길이 +1 해주고 다시 넣어준다.
                else:
                    s[0] += 1
                    stack.append(s)
                    if s[1] == square:
                        flag = False
            if flag:
                stack.append([1, square])

        elif square == stack[-1][1]:
            stack[-1][0] += 1

        else: # square > stack[-1]
            for i in range(len(stack)):
                stack[i][0] += 1
            stack.append([1, square])
    if stack:
        for s in stack:
            result = max(result, s[0]*s[1])
    print(f'{result}\n')


while True:
    arr = list(map(int, input().split(' ')))
    if arr[0] == 0:
        break
    else:
        N = arr[0]
        squares = arr[1:]
        solution(squares)
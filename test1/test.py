#오큰수
import sys
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split(' ')))

def solution():
    stack = deque()
    result = [-1] * N
    for i in range(N):
        # 전에 들어있던 게 현재 것보다 작으면 # 즉 오큰수가 들어오면
        while stack and (stack[-1][0] < arr[i]):
            # stack에는 본인의 idx를 가지고 들어가니까
            tmp, idx = stack.pop()
            result[idx] = arr[i]
        # 본인의 값과 인덱스를 stack에 넣어줌
        stack.append([arr[i], i])
    print(*result)
solution()           
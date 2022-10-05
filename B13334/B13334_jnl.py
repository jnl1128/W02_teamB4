# 시작점
import sys, heapq
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write

N = int(input())
arr = []
for _ in range(N):
    h, o = map(int, input().split(' '))
    if h < o:
        arr.append([o, h])
    else:
        arr.append([h, o])
L = int(input())
# 끝부분이 오름차순이 되도록
# 0번째 : 끝부분, 1번째: 시작부분
arr.sort(key=lambda x:x[0])
# 저장해 둘 곳
stack = []
heapq.heapify(stack)

def solution():
    result = 0
    darr = deque(arr)
    while darr:
        end,start = darr.popleft()
        roadEnd = end
        roadStart = roadEnd-L
        
        heapq.heappush(stack, [start, end])
        
        while stack and stack[0][0] < roadStart:
            heapq.heappop(stack)
        
        result = max(result, len(stack))

    return result

print(solution())

        
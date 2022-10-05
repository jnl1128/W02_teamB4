import sys
import heapq
sys.stdin = open('B13334/B13334_lwh.txt', 'r')
input = sys.stdin.readline

n = int(input())
cases = []
scope = []
ans = 0

# 왼쪽 - 오른쪽 으로 좌표들 입력
for _ in range(n):
    h, o = map(int, input().rstrip().split())
    if h > o :
        cases.append([o, h])
    else:
        cases.append([h, o])

d = int(input())
# 오른쪽 주소 기준 오름차순 
cases.sort(key=lambda x: x[1])

for case in cases:
    left = case[0]
    right = case[1]
    if right - left <= d:
        heapq.heappush(scope, left)
    else:
        continue

    while scope.__len__() > 0 :
        if right - scope[0] <= d:
            break
        else:
            heapq.heappop(scope)
    
    ans = max(ans, len(scope))

print(ans)



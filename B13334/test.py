# 철로
import sys
from queue import PriorityQueue
input = sys.stdin.readline
print = sys.stdout.write

distances = PriorityQueue()

N = int(input())
for _ in range(N):
    h, o = map(int, input().split(' '))
    if h < o:
        distances.put((h, o))
    else:
        distances.put((o, h))
        

D = int(input())

def solution():
    if N == 1:
        print('1')
        return
    curD = distances.get()
    
    result = 0
    while distances.queue:
        if len(distances.queue) +1 < result:
            break
        start = curD[0]
        end = start + D

        nextD = distances.get()

        cnt = 0
        if curD[1] - curD[0] <= D:
            cnt += 1
        if nextD[0] >= start and nextD[1] <= end:
            cnt += 1

        if not distances.queue:
            break

        for distance in distances.queue:
            if distance[0] >= start and distance[1] <= end:
                cnt += 1

        if cnt > result:
            result = cnt

        curD = nextD

    print(f'{result}')

solution()
 
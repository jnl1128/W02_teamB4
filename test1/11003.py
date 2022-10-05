#최솟값 찾기
import sys, heapq
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write

N, L = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

def solution():
    queue = deque([]) #0번째 인덱스: 값, 1번째 인덱스: 인덱스
    for idx, elem in enumerate(arr):
        while queue and queue[-1][0] > elem:
            queue.pop()
        while queue and queue[0][1] < idx-L+1:
            queue.popleft()
        queue.append([elem, idx])
        print(queue[0][0], end = ' ')

solution()
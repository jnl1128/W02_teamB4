import sys
import heapq
sys.stdin = open('B1715/B1715_lwh.txt', 'r')
input = sys.stdin.readline

# min heapify
# heapq 활용
# list를 heap으로 사용할 수 있게 해주는 모듈
# heapq.heappush(list, data)
# heapq.heappop(list)

N = int(input())
card_heap = []
for _ in range(N):
    heapq.heappush(card_heap, int(input()))

sum = 0
while True:
    if card_heap.__len__() == 1:
        break
    temp = heapq.heappop(card_heap) + heapq.heappop(card_heap)
    sum += temp
    heapq.heappush(card_heap, temp)
    
print(sum)

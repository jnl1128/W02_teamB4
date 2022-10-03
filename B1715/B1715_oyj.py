import sys, heapq
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

sumOfCards = 0 
for i in range(n-1) : 
    minA = heapq.heappop(heap)
    minB = heapq.heappop(heap)
    heapq.heappush(heap, minA+minB)
    sumOfCards += minA+minB

print(sumOfCards)
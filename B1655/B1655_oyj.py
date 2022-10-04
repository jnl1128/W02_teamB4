import sys, heapq
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n = int(input())

leftHeap = []
rightHeap = []

def getMidValue(num):
    global leftHeap, rightHeap
    # 1. heappush 과정 
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -1*num) # -num 으로 만들어서 MaxHeap처럼 활용 (나중에 다시 +로 만드는 것 잊지말기)
    else: 
        heapq.heappush(rightHeap, num) # minHeap으로 만들기 

    # 2. 양쪽의 root를 비교해서 왼쪽 heap의 root>오른쪽 heap의 root 이면 swap(heappush)
    if rightHeap and (-1*leftHeap[0]) > rightHeap[0]:
        rightRoot = -1 * heapq.heappop(rightHeap)
        leftRoot = -1 * heapq.heappop(leftHeap)
        heapq.heappush(leftHeap, rightRoot)
        heapq.heappush(rightHeap, leftRoot)
    return -1*leftHeap[0]

for i in range(n):
    num = int(input())
    print(getMidValue(num))

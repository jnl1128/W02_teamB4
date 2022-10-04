# 가운데를 말해요
import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write


def solution():
    N = int(input())
    leftHeap = [] #maxHeap
    rightHeap = [] #minHeap
    heapq.heapify(leftHeap)
    heapq.heapify(rightHeap)

    for i in range(N):
        n = int(input())
        if i == 0:
            heapq.heappush(leftHeap, [-n, n])
        else:
            if len(rightHeap) < len(leftHeap):
                heapq.heappush(rightHeap, [n, n])
            else:
                heapq.heappush(leftHeap, [-n,n])
            
            if leftHeap[0][1] > rightHeap[0][1]:
                leftRoot = heapq.heappop(leftHeap)
                leftRoot[0]*=-1
                rightRoot = heapq.heappop(rightHeap)
                rightRoot[0]*=-1
                heapq.heappush(leftHeap, rightRoot)
                heapq.heappush(rightHeap,leftRoot)
            
        print(f'{leftHeap[0][1]}\n')

solution()
    


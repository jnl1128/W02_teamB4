# 히오스 프로게이머
import sys 
input = sys.stdin.readline
print = sys.stdout.write

def solution():
    N, K = map(int, input().split(' '))
    
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    if N <= 2:
        print(f'{arr[0]+K}')
        return
    start = arr[0]
    end = arr[-1] + K
    result = 0
    while start < end:
        mid = (start+end) //2
        total = 0
        for elem in arr:
            if elem < mid:
                total += mid - elem
        if total > K:
            end = mid
        else:
            result = mid
            start = mid + 1

    print(f'{result}')

solution()

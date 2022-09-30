# 나무자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

def binary():
    start, end = 1, max(arr)
    result = 0
    while start <= end:
        mid = (start+end)//2
        total = 0
        for x in arr:
            if x > mid:
                total += x-mid
        if total < M:
            end = mid -1
        else:
            result = mid
            start = mid + 1
    return result

print(binary())
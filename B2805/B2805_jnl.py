# 나무자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

def binary():
    start, end = 1, max(arr) 
    result = 0
    while start <= end:
        mid = (start+end)//2 # 10
        total = 0
        for x in arr:
            if x > mid:
                total += x-mid
        if total < M:
            end = mid -1 #9
        elif total > M:
            result = mid
            start = mid + 1
        else:
            return mid
    return result

print(binary())
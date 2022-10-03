# 공유기 설치
# 인접한 공유기간의 거리가 최대가 되도록
import sys
input = sys.stdin.readline
print = sys.stdout.write

N,C = map(int, input().split(' '))
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

def solution():
    start = 1
    end = arr[N-1] - arr[0]

    result = 0
    while start <= end:
        mid = (start+end)//2
        cnt = 1
        before = arr[0]
        for c in arr[1:]:
            if c - before >= mid:
                before = c
                cnt += 1
        if cnt >= C:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(f'{result}')
    return

solution()
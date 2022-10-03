#히오스 프로게이머
#전체에 +K만 할 수 있고 최소 레벨이 최대가 되도록
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split(' '))
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

def solution():
    start = arr[0]
    end = arr[N-1] + K

    result = 0
    while start <= end:
        mid = (start+end)//2

        total = 0
        for level in arr:
            if level < mid:
                total += mid - level
        # mid가 최소가 되기엔 너무 커 
        if total > K:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(f'{result}')
    return

solution()


# 두 용액
# 두개의 용액의 합이 0과 가까운 조합을 구하고 싶다
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

def solution():
    result = [20000000001, 0, 0]
    start = 0
    end = N-1

    if N == 2 or arr[start] >= 0:
        print(f'{arr[start]} {arr[start+1]}') 
        return
    elif arr[end] <= 0:
        print(f'{arr[end-1]} {arr[end]}')
        return

    while start < end:
        mid = arr[start] + arr[end]
        # 더 좋은 result가 나옴
        if abs(mid) < result[0]:
            result = [abs(mid), arr[start], arr[end]]
        
        if mid < 0:
            start += 1
        elif mid == 0:
            print(f'{result[1]} {result[2]}')
            return
        else: 
            end -= 1

    print(f'{result[1]} {result[2]}')
    return

solution()
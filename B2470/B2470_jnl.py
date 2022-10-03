# 두 용액 #통과 #완벽 이해는 못함
import sys
input = sys.stdin.readline
print = sys.stdout.write

def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))
    arr.sort()
    end = N-1
    start = 0

    if N == 2 or arr[start] >= 0:
        print(f'{arr[start]} {arr[start+1]}')
        return
    if arr[end] <= 0:
        print(f'{arr[end-1]} {arr[end]}')
        return

    a = [ 20000000001, 0, 0]
    while start < end:
        mid = arr[end] + arr[start]
        if abs(mid) < a[0]:
            a[0] = abs(mid)
            a[1] = start
            a[2] = end

        if mid < 0: # better 음수
            start += 1
        
        elif mid > 0: # better 양수
            end -= 1
        
        else:
            break

    print(f'{arr[a[1]]} {arr[a[2]]}')
        
solution()

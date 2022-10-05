#랜선 만들기
import sys
input = sys.stdin.readline
print = sys.stdout.write

K, N = map(int, input().split(' '))
lan = []
for _ in range(K):
    lan.append(int(input()))
lan.sort()

def solution():
    start = 1
    end = lan[K-1]
    result = 0
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for l in lan:
            cnt += l//mid
        if cnt >= N:
            result = mid
            start = mid + 1
        else:
            end = mid -1
    print(f'{result}')

solution()   

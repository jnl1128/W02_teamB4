import sys
sys.stdin = open('B16564/input_lwh.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
Xs = [int(input()) for _ in range(N)]

def find_T(K):
    low, high = min(Xs), max(Xs)+K
    ans = 0
    while True:
        T = (low + high) // 2
        total = 0
        for X in Xs:
            if X < T:
                total += T - X
        if total == K:
            return T
        elif total < K: # 레벨 더 올려도 됨
                low = T + 1
                ans = T
        else:   # 레벨 너무 올림 줄여야 함
            high = T - 1
        if low > high:
            break
    return ans

print(find_T(K))












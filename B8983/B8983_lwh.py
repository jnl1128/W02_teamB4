import sys
sys.stdin = open('B8983/B8983_lwh.txt', 'r')
input = sys.stdin.readline

def be_food(fires, prey, L):
    x, y = prey[0], prey[1]
    left, right = 0, len(fires) - 1 # = M -1
    target = L - y 

    while True:
        mid = (left + right) // 2
        if abs(fires[mid] - x) <= target:
            return True
        elif fires[mid] < x:   # 왼쪽으로 너무 멀어
            left = mid + 1
        else:           # 오른쪽으로 너무 멀어 
            right = mid -1
        if left > right:
            return False

def init():
    M, N, L = map(int, input().split())
    fires = sorted(list(map(int, input().split())))
    count = 0
    for _ in range(N):
        x, y = list(map(int, input().split()))
        if y > L:
            continue
        else:
            prey = [x, y]
            if be_food(fires, prey, L):
                count += 1

    print(count)

init()


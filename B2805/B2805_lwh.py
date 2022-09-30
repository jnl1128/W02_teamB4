import sys
sys.stdin = open('B2805/input_lwh.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def find_H(trees, M):
    low, high = 1, max(trees) # O(n)
    ans = 0
    while True:
        H = (low+high) // 2
        in_hand = 0
        # trees_filtered = list(filter(lambda tree: tree > H, trees))
        # in_hand = sum(trees_filtered) - H*len(trees_filtered)
        for tree in trees:
            if tree > H:
                in_hand += tree - H
        if in_hand == M:
            return H
        elif in_hand < M:
            high = H - 1
        else:
            low = H + 1
            ans = H
        if low > high:
            break
    return ans

print(find_H(trees, M))



import sys
sys.stdin = open('B1920/input_lwh.txt', 'r')
input = sys.stdin.readline

def bi_search(arr, key):
    pl = 0
    pr = len(arr) - 1
    while True:
        pc = (pl + pr) // 2
        if arr[pc] == key:
            return 1
        elif arr[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0
        
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
keys = list(map(int, input().split()))

arr = sorted(arr)
for key in keys:
    print(bi_search(arr, key))






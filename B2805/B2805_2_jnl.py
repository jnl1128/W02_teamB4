# 나무 자르기
# 높이가 H보다 높으면 잘리고
# 그 잘린 부분들의 합이 M이상이고 싶고, H를 최대로 하고 싶다
import sys
input = sys.stdin.readline
print = sys.stdout.write

N,M = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))
trees.sort()

def solution():
    start = 1
    end = trees[N-1]

    result = 0
    while start <= end:
        height = (start + end)//2

        total = 0
        for tree in trees:
            if tree > height:
                total += tree - height

        # height를 지금보다 높여도 될거 같은데
        if total == M:
            print(f'{height}')
            return
        elif total >  M:
            start = height + 1
            result = height
        else:
            end = height - 1
    
    print(f'{result}')
    return

solution()

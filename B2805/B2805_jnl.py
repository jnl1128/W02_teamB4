# 나무자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))

def binary():
    start, end = 1, max(trees) 
    result = 0
    while start <= end:
        # 현재 자르고 싶은 나무의 높이
        height = (start+end)//2 
        total = 0
        for tree in trees:
            if tree > height:
                total += tree - height
        if total == M:
            return height
        elif total < M:
            # 지금 자르려고 한 높이는 너무 낮아
            end = height -1
        else:
            # else문으로 들어온다는 것은 일단 M보다는 많이 가져갈 수 있다는 것
            # result에 갱신해야 하는 이유: total == M이 안되는 상황이 와도, 적어도 M보다 많이 가져갈 수 있는 높이를 알기 위해
            result = height
            # 지금 자르려고 한 높이는 너무 높아
            start = height + 1
    return result

print(binary())
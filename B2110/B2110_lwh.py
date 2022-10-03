import sys
sys.stdin = open('B2110/B2110_lwh.txt', 'r')
input = sys.stdin.readline

def route():
    res = 0
    left, right = 1, houses[-1] - houses[0]

    while left <= right:
        mid = (left + right) // 2
        count = 1
        wifi = houses[0]

        for idx in range(1, N):
            if houses[idx] >= wifi + mid:
                count += 1
                wifi = houses[idx]
        if count < C:
            right = mid - 1
        else:
            left = mid + 1
            res = mid
    return res

# https://western-sky.tistory.com/128
# 집 좌표 최대 크기가 10억이므로, 순차탐색이 아닌 이분탐색을 떠올려볼 것
# 공유기 간 최대거리를 찾는 것이 목적이므로 이분탐색 활용할 것
# left <= right일 동안 아래 과정을 반복하며 중간값이 최대가 되는 값은 탐색한다.
# 중간값 mid = (left+right)//2로, 최초 공유기 개수는 1, 최초 공유기 위치는 house[0]으로 설정한다.
# 반복문을 돌며 2번째 집부터 마지막 집까지 아래 조건을 체크한다.
# i번째 집 좌표가 이전 공유기 위치로부터 + 최대거리(중간값 mid)을 넘어서면 새로운 공유기를 설치하고, 공유기 개수를 증가시킨다.
# 반복문 종료 후, 공유기 개수가 c보다 작다면 최대거리가 긴 것이므로 right = mid - 1
# 공유기 개수가 c보다 크다면 최대거리가 짧은 것이므로 answer에 최대거리 저장 후 left = mid + 1
# answer를 출력한다.

N, C = list(map(int, input().split()))
houses = [int(input()) for _ in range(N)]
houses = sorted(houses)

print(route())
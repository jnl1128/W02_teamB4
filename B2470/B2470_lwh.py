import sys
sys.stdin = open('2407.txt', 'r')
input = sys.stdin.readline


# https://latte-is-horse.tistory.com/316
# 1. 용액들을 정렬한다
# 2. 정렬된 용액들을 순차적으로 방문한다
# 3. 현재 방문한 용액이 10번째이고, -99의 값을 가지고 있다면 11번째부터 마지막 용액까지 중에 
#    -99와 더했을 때 0을 만들 수 있는 +99와 가장 가까운 용액을 이분 탐색으로 찾는다
# 4. 3번에서 찾은 값이 +99와 가장 가까운 값이 아닐 수도 있다. 
#   용액들이 정렬되어 있기 때문에 3번에서 찾은 값의 바로 옆에 있는 값을 같이 확인해봐야 한다
#   4-1.아래 코드에서는 이분 탐색으로 찾은 값과 그 왼쪽의 값을 비교했다. 
#       이분 탐색 과정에서 arr[mid] >= target 일 때 res를 갱신했으므로 
#       찾은 값보다 더 오른쪽에 있는 값은 답이 아니게 된다
# 5. 용액들을 순차적으로 방문하며 3, 4번의 과정을 반복하다가 현재 가장 0과 가까워지는 수를 찾았다면 
#    이를 갱신하며 최종적으로 가장 0과 가까운 두 수를 찾는다

N = int(input())
arr = sorted(list(map(int, input().split())))
# print(attr_list)

def binary_search(idx, target):
    res = N-1
    start, end = idx, N - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
            res = mid
        else:
            start = mid + 1
    return res

def solution():
    v1, v2 = 0, 0
    best_sum = 10 ** 10
    for i in range(N):
        # 이분 탐색 수행: 현재 위치(i) 이후의 용액에서 탐색, 찾는 값은 (현재 용액 * -1)
        res = binary_search(i + 1, -arr[i])
        
        # 찾은 용액의 왼쪽 용액 확인
        if i + 1 <= res - 1 < N and abs(arr[i] + arr[res - 1]) < best_sum:
            best_sum = abs(arr[i] + arr[res - 1])
            v1, v2 = arr[i], arr[res - 1]

        # 찾은 용액 확인
        if i + 1 <= res < N and abs(arr[i] + arr[res]) < best_sum:
            best_sum = abs(arr[i] + arr[res])
            v1, v2 = arr[i], arr[res]

    print(v1, v2) # i 번째 용액을 확인할 때 i + 1번 용액부터 확인하기 때문에 항상 v1 <= v2 이다.


solution()
# 수 찾기
# 이진탐색이란?
    # 정렬되어 있는 배열에서 특정한 값을 찾아내는 알고리즘
    # 배열의 중간에 있는 임의의 값을 선택하고 찾고자 하는 값 x와 비교한다.
    # x가 중간값보다 작으면 중간 값을 기준으로 좌측의 데이터들을 대상으로,
    # x가 중간값보다 크면 배열의 우측을 대상으로 다시 탐색한다.
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arrN = list(map(int, input().split(' ')))
M = int(input())
arrM = list(map(int, input().split(' ')))

# 오름차순으로 정렬
arrN.sort()

def solution(num):
    startIdx = 0
    endIdx = N
    midIdx = (startIdx+endIdx)//2
    while startIdx < endIdx:
        if num == arrN[midIdx]:
            return True
        elif num > arrN[midIdx]:
            startIdx = midIdx+1
        else:
            endIdx = midIdx
        midIdx = (startIdx+endIdx)//2
    return False


for numM in arrM:
    if solution(numM):
        print('1\n')
    else:
        print('0\n')

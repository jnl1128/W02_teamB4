# 수 찾기 #2nd 
# A[]를 정렬하고
# start = 0 # end = len(A[])-1
# mid = (start + end)//2

# B[i]가 A[mid]보다 크면 start = mid + 1
# B[i]가 A[mid]보다 작으면 end = mid - 1
# B[i]가 A[mid]이면 1출력하고 while 문 탈출
# 위의 과정을 start<=end인 경우에만 

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = list(map(int, input().split(' ')))
A.sort()

M = int(input())
B = list(map(int, input().split(' ')))



def contain(num):
    start = 0 
    end = N-1
    while start <= end:
        mid = (start + end)//2
        if num < A[mid]:
            end = mid -1
        elif num >A[mid]:
            start = mid + 1
        else:
            return True
    return False

def solution():
    for b in B:
        if contain(b):
            print('1\n')
        else:
            print('0\n')

solution()
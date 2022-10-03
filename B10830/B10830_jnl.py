# 행렬제곱
import sys
input = sys.stdin.readline
print = sys.stdout.write
N, B = map(int, input().split(' '))

def solution():
    global N, B
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split(' '))))

    matrix = modMatrix(matrix, 1000)

    resultMatrix = DC(B, matrix)

    for i in range(N):
        for j in range(N):
            print(f'{resultMatrix[i][j]} ')
        print('\n')

# 제곱
def matrixMultiply(arr):
    global N
    D2Matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                D2Matrix[i][j] += arr[i][k]*arr[k][j]
        D2Matrix[i][j] %= 1000 
    return D2Matrix

# B가 홀수인 경우에 인풋으로 주어진 행렬과 곱해줄 용도
def matrixMultiply2(arr1, arr2):
    D2Matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                D2Matrix[i][j] += arr1[i][k]*arr2[k][j]
        D2Matrix[i][j] %= 1000
    return D2Matrix

def modMatrix(arr, n):
    global N
    for i in range(N):
        for j in range(N):
            arr[i][j] %= n
    return arr

def DC(b, arr):
    if b == 1:
        return arr
    half = DC(b//2, arr)
    m = matrixMultiply(half)
    m = modMatrix(m, 1000)
    if b % 2 != 0:
        mm = matrixMultiply2(arr, m)
        m = modMatrix(mm, 1000)
    return m
       
solution()           
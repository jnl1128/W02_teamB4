import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('B10830/B10830_lwh.txt', 'r')
input = sys.stdin.readline

N, B = list(map(int, input().split()))
matrix = [[*list(map(int, input().split()))] for _ in range(N)]
depth = 0

def square0(matrix):
    squared = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):

                squared[i][j] += matrix[i][k]*matrix[k][j]
            squared[i][j] %= 1000
    return squared

def square(matrix1, matrix2):
    squared = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                squared[i][j] += matrix1[i][k]*matrix2[k][j]
            squared[i][j] %= 1000
    return squared

def power(B):
    global depth
    depth += 1

    # if B == 2:
    #     return square(matrix, matrix)
    # elif B == 3:
    #     return square(square0(matrix), matrix)

    if B == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000
        return matrix

    mat = power(B//2)

    if B % 2 == 0: # 짝수일 때
        B //= 2
        return square0(mat)
    else: # 홀수일 때
        B //= 2
        return square(square0(mat), matrix)

for row in power(B):
    print(*row) # 좋은거
print(depth)


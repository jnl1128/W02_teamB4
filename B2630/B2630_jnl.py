#색종이만들기
import sys
input = sys.stdin.readline

blue = 0
white = 0
N = int(input()) #N는 2의 제곱수
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split(' '))))

def solution(width, r, c):
    global blue, white

    if width == 1:
        if matrix[r][c] == 1:
            blue += 1
        else:
            white += 1
        return
    
    color = matrix[r][c]
    for i in range(r, r+width):
        for j in range(c, c+width):
            if color != matrix[i][j]:
                solution(width//2, r, c)
                solution(width//2, r+width//2, c)
                solution(width//2, r, c+width//2)
                solution(width//2, r+width//2, c+width//2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1
                
solution(N, 0, 0)
print(white, blue, sep ='\n', end='')

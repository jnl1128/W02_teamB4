import sys
sys.stdin = open('B2630/input_lwh.txt', 'r')
input = sys.stdin.readline

def cut_paper(x, y, n):
    global white, blue
    init = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != init:
                for k in range(2):
                    for l in range(2):
                        cut_paper(x+k*n//2, y+l*n//2, n//2)
                return
    if init == 0:
        white += 1
    elif init == 1:
        blue += 1
    return

white = 0
blue = 0

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cut_paper(0, 0, N)
print(white)
print(blue)

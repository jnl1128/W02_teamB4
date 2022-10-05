import sys
import math
from collections import deque
sys.stdin = open('B3190/B3190_lwh.txt', 'r')
input = sys.stdin.readline

def crawl(board, snake, X, dx, dy):
    global time
    global GAME_OVER
    move = True
    while True:
        if time == X and move:
            return
        if move:
            head = (snake[0][0]+dx, snake[0][1]+dy)
            board[head[0]][head[1]] *= board[head[0]-dx][head[1]-dy]
            snake.appendleft(head)
            time +=1
        elif (not move) and board[head[0]][head[1]] == 3: # and not apple
            tail = snake.pop() # tail 제거
            board[tail[0]][tail[1]] = 1
        elif (not move) and board[head[0]][head[1]] == 6: # apple
            board[head[0]][head[1]] //= 2
        
        move = not move
        
        if board[head[0]][head[1]] == 0:
            GAME_OVER = True
            return 
        if board[head[0]][head[1]] == 9:
            GAME_OVER = True
            return


def start(board, commands):
    global time
    global GAME_OVER
    game_over = False
    snake = deque([(1, 1)])
    # direction
    d = 0 
    # while not game_over:
    for command in commands:
        X, C = command

        dx = round(-math.sin(math.pi * (d/2)))
        dy = round(math.cos(math.pi * (d/2)))
 
        X = int(X)
        crawl(board, snake, X, dx, dy)
       
        if C == 'D':
            d -= 1
        elif C == 'L':
            d += 1
    
        if GAME_OVER:
            return

    dx = round(-math.sin(math.pi * (d/2)))
    dy = round(math.cos(math.pi * (d/2)))
    
    crawl(board, snake, 10000, dx, dy)
    
    if GAME_OVER:
        return

def init(N, apples, commands):
    global time
    # init board, wall(0)
    board = [[1]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        board[0][i] = 0
        board[N+1][i] = 0
        board[i][0] = 0
        board[i][N+1] = 0
    
    # init apples(2)
    for apple in apples:
        x, y = apple[0], apple[1]
        board[x][y] = 2
    
    # init snake(3)
    board[1][1] = 3

    start(board, commands)
    
N = int(input())    # 보드의 크기   2<= N <= 100 
K = int(input())    # 사과의 개수   0<= K <= 100
apples = [list(map(int, input().split())) for _ in range(K)]   # 사과의 위치 [행, 열]
L = int(input())    # 방향 변환 횟수    1<= L <= 100
commands = [input().split() for _ in range(L)]
time = 0
GAME_OVER = False
init(N, apples, commands)
print(time)
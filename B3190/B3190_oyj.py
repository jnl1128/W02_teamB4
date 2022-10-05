import sys
from collections import deque
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

# 입력값 받기 및 초깃값 셋팅 
N = int(input())

# n*n 크기의 보드 생성 [1행:[1열 2열 3열 .. N열] 2행:[] ... N행[]]
board = []
for i in range(N):
    temp_row = []
    for j in range(N):
        temp_row.append(0)
    board.append(temp_row)

# 사과의 위치 (보드의 해당 칸의 값이 1)
K = int(input())
for i in range(K):
    row,column = map(int,input().split())
    board[row-1][column-1] = "A"

L = int(input()) #방향전환은 시간에 따라 순차적으로 발생
# 뱀의 머리가 향하는 방향
snake_direction = "R" # U은 위, R는 오른쪽 D는 아래 L은 왼쪽
current_direction = 0

direction= deque()
for i in range(L):
    X,C = input().split()
    X = int(X)
    rotate = ['R','D','L','U']
    
    if C == 'D':
        current_direction = (current_direction+1)%4
        C = rotate[current_direction]
    else:  
        current_direction = (current_direction-1)%4
        C = rotate[current_direction]
    direction.append([X,C])

#시간(초) 1초씩 올라가면 움직임을 시행한다. 
time_second = 0  


#뱀 
snake = deque()
snake.append([0,0])

#뱀의 다음 스텝
def whereToGo(snakeHead) :
    global snake_direction, snake
    if snake_direction == "R":
    # 행은 그대로, 열은 +1 
        nextStep = [snakeHead[0], snakeHead[1]+1]
        return nextStep
    elif snake_direction == "L":
        # 행은 그대로, 열은 -1 
        nextStep = [snakeHead[0], snakeHead[1]-1]
        return nextStep
    elif snake_direction == "U":
        # 행은 -1,열은 그대로
        nextStep = [snakeHead[0]-1, snakeHead[1]]
        return nextStep
    else: #snake_direction == "D"
        # 행은 +1,열은 그대로
        nextStep = [snakeHead[0]+1, snakeHead[1]]
        return nextStep

def isThereApple():
    global board, snake  # 뱀의 머리 위치(행,렬)로 board에서 해당 위치를 찾아서 사과가 있다면
    if board[snake[-1][0]][snake[-1][1]] == "A" :
        board[snake[-1][0]][snake[-1][1]] = 0
        return True
    else :
        return False

def isGameOver(nextStep, N):
    global snake
    # 벽에 닿았는지 확인 
    if nextStep[0]< 0 or nextStep[0]>= N or nextStep[1]< 0 or nextStep[1]>= N :
        return True
    # 몸에 닿았는지 확인
    elif nextStep in snake :
        return True
    else:
        return False
        

while True:
     # 초가 1 증가한다. 벽이나 몸에 닿는지(게임 끝인지) 확인하기 전에 초수를 늘려나야 정확히 게임이 끝나는 시간을 포착할 수 있다.  
    time_second+=1 # 1초씩 증가

    # 다음 갈 곳을 찾는다
    nextStep = whereToGo(snake[-1])

    # 다음 갈 곳이 벽이나 몸에 닿는다면 시간을 출력하고 게임을 끝낸다.  
    if isGameOver(nextStep, N):
        print(time_second)
        break 

    # 다음 갈 곳으로 이동한다
    snake.append(nextStep)

    # 사과가 있는지 확인 후 없으면 꼬리를 자른다
    if isThereApple() == False :
        snake.popleft()
    # print(f'{time_second}초 후 뱀은 {snake}')
    
     # 현재 초에서 방향을 전환해야 하는지 확인한다. '게임 시작 시간으로부터 X초가 끝난 뒤에 '
    if direction and direction[0][0] == time_second :
        snake_direction = direction[0][1]
        direction.popleft()
   
   
    




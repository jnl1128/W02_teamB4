import sys
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


# 다음에 가는 곳이 벽인지
# 다음에 가게 되면 몸과 부딪히는지

# 죽지 않았다면 현재 있는 곳에 사과가 있는지

# 방향을 바꿀 타이밍인지



N = int(input().rstrip())
apple = [[0]*N for _ in range(N)]
K = int(input().rstrip())
for _ in range(K):
    row, col = map(int, input().rstrip().split(' '))
    # 왜 그러니
    apple[row-1][col-1] = 1
D = int(input().rstrip())
dir = deque([])
for _ in range(D):
    # rstrip 안해서 이 사단이 난거였음
    t, d = input().rstrip().split(' ')
    dir.append([int(t), d])
    

def game_over(loc, snake):
    if loc[0] < 0 or loc[0] > N -1:
        return True
    if loc[1] < 0 or loc[1] > N -1:
        return True
    for s in snake:
        if s[0] == loc[0] and s[1] == loc[1]:
            return True
    return False

time = 0
s_loc = deque([[0,0]])
s_dir = [0,1]
while True:
    time += 1
    next_loc = [s_loc[-1][0]+s_dir[0], s_loc[-1][1]+s_dir[1]]
    
    if game_over(next_loc, s_loc):
        break

    flag = True
    # 사과가 있는 경우
    if apple[s_loc[-1][0]][s_loc[-1][1]] == 1:
        apple[s_loc[-1][0]][s_loc[-1][1]] = 0
        flag = False
    
    s_loc.append(next_loc)

    if s_loc and flag:
        s_loc.popleft()
    

    if dir and dir[0][0] == time:
        if dir[0][1] == 'D':
            s_dir[0], s_dir[1] = s_dir[1], -s_dir[0]
        else:
            s_dir[0], s_dir[1] = -s_dir[1], s_dir[0]
        dir.popleft()

print(f'{time}')

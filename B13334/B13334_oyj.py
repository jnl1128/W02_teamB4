import sys, heapq
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
roads = []
for i in range(N):
    road = sorted(list(map(int,input().split())))
    roads.append(road)

D = int(input())
roads.sort(key=lambda x:x[1]) #끝나는 지점을 기준으로 오름차순

included = [] # 철로에 포함되는 도로들 (MinHeap)
candidates = [] # 철로가 움직일 때마다 철로에 포함되는 집들의 수 
for i in range(N):
    if roads[i][1]-roads[i][0] > D : # 도로가 철로보다 길다면 따질 필요 없음. 다음으로 넘어간다
        continue
    
    heapq.heappush(included, roads[i])# 현재 확인하는 도로를의 왼쪽 값을 included에 heappush
    
    # 현재 확인하는 도로의 오른쪽 값에 나무 철로의 오른쪽이 오게 위치시켰을 때의 왼쪽 끝값을 저장 
    # 적어도 이보단 커야 철로에 포함될 수 있다
    rail_left = roads[i][1] - D 
    
    while True: 
        if included[0][0] < rail_left :
            heapq.heappop(included) # rail_left 보다 작은 도로는 pop
        else: #가장 작은 값이 rail_left 이상이면 빠져나온다
            break
    
    # 모든 pop을 끝내고 나서 included 에 남아있는 도로의 수를 기록하여 max 값을 찾는다
    candidates.append(len(included))

if candidates :
    print(max(candidates))
else :
    print(0)
    

# print(f'N : {N}')
# print(f'roads : {roads}')
# print(f'D : {D}')


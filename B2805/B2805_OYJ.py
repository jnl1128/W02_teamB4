import sys
sys.stdin = open("input.txt","r")
n,m = list(map(int,sys.stdin.readline().split()))
trees = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)
min_h, max_h = 1, max(trees)

while True: 
    mid_h = (min_h+max_h)//2
    wood=0
    for tree in trees :
        if tree > mid_h :
            wood += tree - mid_h
        else: # 나무의 길이가 h보다 작다면 (안 잘리면) 더 이상 반복문을 실행할 필요없음 
            break 
    if wood == m :
        break
    elif wood < m: # 더 작은 h를 찾아야 해
        max_h = mid_h -1
    else: # 더 큰 h를 찾아야 해
        min_h = mid_h +1
    if min_h > max_h:
        break

print(mid_h) 
# 와의 정확한 차이점이란....?
print((min_h+max_h)//2)


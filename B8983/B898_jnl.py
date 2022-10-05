# 사냥꾼
import sys
from collections import deque
input = sys.stdin.readline
print= sys.stdout.write

M, N, L = map(int, input().split(' '))
guns = list(map(int, input().split(' ')))
guns.sort()
huntRange = []
animals = []
for _ in range(N):
    x, y = map(int, input().split(' '))
    animals.append([x, y])

def solution():
    cnt = 0
    for animal in animals:
        start = 0
        end = M-1
        mid = (start + end)//2
        gun = guns[mid] 

        if animal[1] > L:
            continue

        if abs(animal[0] - gun) + animal[1] <= L:
            cnt+= 1
            continue
        else:
            while start <= end:
                if animal[0] < gun:
                    end = mid -1
                else:
                    start = mid +1
                mid = (start+end)//2
                gun = guns[mid]
                if abs(animal[0] - gun) + animal[1] <= L:
                    cnt += 1
                    break
    print(f'{cnt}')
            
solution()
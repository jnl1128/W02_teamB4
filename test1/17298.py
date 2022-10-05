#오큰수
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = deque(list(map(int, input().split(' '))))
curMax = 0
def solution():
    global curMax
    while arr:
        a = arr.popleft()
        if not arr:
            print('-1')
            break
        flag = True
        if a < curMax:
            print(f'{curMax} ')
            continue
        for e in arr:
            if e > a:
                print(f'{e} ')
                curMax = e
                flag = False
                break
        if flag:
            print('-1 ')

solution()

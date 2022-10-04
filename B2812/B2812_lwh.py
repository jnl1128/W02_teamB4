import sys
from collections import deque
sys.stdin = open('B2812/B2812_lwh.txt', 'r')
input = sys.stdin.readline

N, K = list(map(int, input().split()))
number = input().rstrip()
result = ''
stack = deque([])

for idx, num in enumerate(number):
    pos = len(result)
    
    while stack and int(stack[-1]) < int(num):
        stack.pop()
    stack.append(num)
    
    if idx == (K + pos): # N - (N-K) + pos
        result += stack.popleft()

print(result)

# K 번 까지중에 제일 큰 digit push() 
# push한 digit의 idx의 다음 부터 K-1 개중 제일 큰 digit push()
# ... 
# K = 0 되면 그대로 push()
# 출력


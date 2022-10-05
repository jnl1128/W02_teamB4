#moo 게임
import sys
input = sys.stdin.readline
# print = sys.stdout.write


def sol1(n):
    if n == 0:
        return 3
    half = sol1(n-1)
    return half*2 + n+3

def solution(depth):
    if depth == 1:
        return 'moomooomoo'
    half = solution(depth-1)
    return half + 'mooo'+'o'*(depth-1) +half

N = int(input())
recurTime = 0
if N == 1:
    print('m')
elif N == 2 or N==3:
    print('o')
else:
    for i in range(1, N):
        if sol1(i) >= N:
            recurTime = i
            break
    mStr = solution(recurTime)
    print(mStr)
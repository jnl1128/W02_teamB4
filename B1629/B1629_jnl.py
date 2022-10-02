#곱셈
import sys
input = sys.stdin.readline
print = sys.stdout.write
A, B, C = map(int, input().split(' '))

def solution(B, AC):
    global C
    if B == 1:
        return AC
    half = solution(B//2, AC)
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * AC) % C

if A == C:
    print('0')
elif A == 1:
    print('1')
else:
    print(f'{solution(B, A%C)}')

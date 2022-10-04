import sys
sys.stdin = open('B1629/B1629_lwh.txt', 'r')
input = sys.stdin.readline


def power(A, B):
    A %= C
    if B == 1:
        return A

    A2 = power(A, B//2)
    A %= C

    if B % 2 == 0:
        B //= 2
        A2 **= 2
        A2 %= C
        return A2
    else:
        B //= 2
        A2 = ((A2**2)%C) * A 
        A2 %= C
        return A2

A, B, C = list(map(int, input().split()))
print(power(A, B))
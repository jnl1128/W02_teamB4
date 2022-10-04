import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

a,b,c = list(map(int,input().split()))

def get(a,b,c) :
    if b==1 :
        return a%c
    half = get(a,b//2,c)%c
    if b%2 == 0 : #짝수이면
        return (half*half)%c
    else: #홀수이면
        return (half*half*a)%c
    
print(get(a,b,c))

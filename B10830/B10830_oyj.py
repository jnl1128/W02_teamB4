import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
# 입력
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

N,b = map(int,input().split())
matrix = [] # 2차원 배열로 행렬 생성
for i in range(N):
    matrix.append((list(map(int,input().split()))))

def getMod(bigMatrix,n):
    for i in range(n):
        for j in range(n):
            bigMatrix[i][j] = bigMatrix[i][j]%1000
    return bigMatrix

def productEven (A,n) :
    nextM =[]
    for x in range(n):
        tempM =[]
        for y in range(n):
            temp =0
            for z in range(n):
                temp += A[x][z]*A[z][y]
            temp = temp%1000
            tempM.append(temp)
        nextM.append(tempM)
    return nextM

def productOdd (A,B,n) :
    nextM =[]
    for x in range(n):
        tempM =[]
        for y in range(n):
            temp =0
            for z in range(n):
                temp += A[x][z]*B[z][y]
            temp = temp%1000
            tempM.append(temp)
        nextM.append(tempM)
    return nextM

def powerOf(A,B,n):
    if B ==1 :
        return getMod(A, n)
    else: 
        half = powerOf(A,B//2,n)
        powerOfTwo = productEven(half, n)
        if B%2 ==0 :
            return powerOfTwo
        else:
            return productOdd(powerOfTwo, A, n)

result = powerOf(matrix,b,N)

for element in result:
    print(*element)


# 문제
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오.
#  수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.


# 출력
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다
from collections import deque
N = int(input())
def getMoo(totalMoo, middle, N):
    left = (totalMoo - middle)//2
    # 왼쪽에 있는지
    if N <= left:
        return getMoo(left, middle -1, N)
    # 오른쪽에 있는지
    elif N>left+middle:
        return getMoo(left, middle-1, N-left-middle)
    # 가운데에 있는지
    else:
        return 'o' if N-left-1 else 'm'


def solution():
    
    if N == 1:
        print('m')
        return
    elif N<= 3:
        print('o')
        return
    else:
        moo,recurTime = 3,0
        while moo < N:
            recurTime += 1
            moo = moo * 2 + recurTime + 3
        
        print(getMoo(moo,recurTime+3,N))
solution()
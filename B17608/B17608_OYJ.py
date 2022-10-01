import sys
sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())

def get_sum_of_stack(stk):
    sum_stk = 0 
    for i in stk :
        if i ==None:
            break
        else: 
            sum_stk += 1
    return sum_stk 

def get_stack(n) :
    stk = [None]*n 
    ptr = 0 
    for i in range(n):
        stick = int(sys.stdin.readline())
        if ptr == 0 :
            stk[ptr] = stick 
            ptr+=1
            continue
        # 이전 포인터의 길이보다 더 작을 때까지 계속 삭제, ptr가 0이되면 push 
        while stk[ptr-1] <= stick :
            stk[ptr-1] = None
            ptr-=1
            if ptr == 0 :
                break
        if ptr == 0 :
            stk[ptr] = stick 
            ptr+=1
            continue
        stk[ptr] = stick
        ptr +=1 
    return stk

stack = get_stack(n)
print(get_sum_of_stack(stack))

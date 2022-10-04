import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n,k = map(int,input().split())
num = input() # '1924'

stack =[]
atLeast = n-k
end= False


for i in range(len(num)): # input으로 받은 숫자 한글자씩 순회
    if i==0: # 0번째 숫자라면 바로 stack에 push
        stack.append(num[i])
    else: # 1번째 이후 숫자라면 answer와 비교하면서 순회 시작
        for j in range(len(stack)-1, -1, -1):
            # 비교할 형편이 되니???
            if len(stack)+(n-i) <= atLeast:
                remainingNum = num[i:]
                end = True
                break
            if stack[j] < num[i] :
                stack.pop()
            else : 
                # 이전 숫자보단 작지만 추가해도 되니? (n-k보다 같거나 작니?) 
                if len(stack)< atLeast :
                    stack.append(num[i])
                break
        if end==True :
            break
        if len(stack) == 0: # 반복문을 다돌았는데 길이가 0이면 (아무 요소도 없다면)
            stack.append(num[i])
        
stack = list(map(int, stack))

for i in stack :
    print(i,end="")
print(remainingNum)



    



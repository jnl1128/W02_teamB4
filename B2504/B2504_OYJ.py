import sys
sys.stdin = open("input.txt","r")
string= sys.stdin.readline().strip()
stack = [None]*len(string)
ptr = 0
wrong= False
depth = []
temp= []

def open():
    depth.append(1)
    temp.append(0)

def close(a):
    i = len(depth)
    if len(depth) == len(temp) :
        temp[i-1] += a
    elif temp[i] != 0:
        temp[i-1] += temp[i]*a
        temp[i] = 0 
    else:
        temp[i-1] += a
    del depth[i-1]

for i in range(len(string)):
    # 옳은 괄호열인지 체크 
    if string[i] == '(' or string[i] == '[': # 여는 괄호는 묻따 push
        stack[ptr] = string[i] 
        ptr +=1
        open()
    elif string[i] == ')':
        if ptr == 0 :
            wrong = True
        elif stack[ptr-1] == '(' : # 쌍이 맞으므로 pop 
            stack[ptr-1] = None
            ptr -=1
            close(2)
        else :
            wrong = True
    else : # 닫는 대괄호 ] 
        if ptr == 0 :
            wrong = True
        elif stack[ptr-1] == '[' : # 쌍이 맞으므로 pop 
            stack[ptr-1] = None
            ptr -=1
            close(3)
        else :
            wrong = True
    
#옳은 괄호열인 경우에 (옳지 않은 경우 이미 break로 탈출)
if wrong: 
    print(0)
else :
    print(temp[0])



## 초기 코드 
# for i in range(len(string)):
#     if ptr == 0:
#         if string[i] == ')' or string[i] == ']':
#             print(0)
#             break
#         else:  
#            stack[ptr] = string[i]
#            ptr +=1
#     else:
        # # 첫번째에 push하는 경우가 아닌 경우 - 케이스를 나누어 생각해야 한다.
        # if stack[ptr-1] == '(':
        #     if string[i] == '(' or string[i] == '[':
        #         stack[ptr] = string[i]
        #         ptr +=1
        #     elif string[i] == ')':
        #         stack[ptr-1] = None
        #         ptr -=1
        #     else: # ]인 경우 
        #         wrong= True
        # else : # stack[ptr-1] = '['
        #     if string[i] == '(' or string[i] == '[':
        #         stack[ptr] = string[i]
        #         ptr +=1
        #     elif string[i] == ']':
        #         stack[ptr-1] = None
        #         ptr -=1
        #     else: # ]인 경우 
        #         print(0)
        #         break
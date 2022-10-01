import sys
sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().strip()
    parenthesis = [None]*len(line)
    ptr = 0 
    for j in range(len(line)):
        if line[j] == '(' :
            parenthesis[ptr]= line[j]
            ptr+=1 
        else:
            del parenthesis[ptr-1]
            ptr-=1 
        if ptr < 0 :
            print("NO")
            break
    if ptr>=0 and parenthesis[0] == None :
        print("YES")
    if ptr>=0 and parenthesis[0] != None :
        print("NO")

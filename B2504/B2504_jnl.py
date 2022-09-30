#괄호의 값
import sys
input = sys.stdin.readline
# print = sys.stdout.write

def solution():
    ps = list(input().rstrip())
    if len(ps) % 2 !=0: 
        print('0')
        return 
    depth = [0] * (len(ps))
    D = [0] * len(ps)
    stack = []
    for p in ps:
        if p =='(' or p == '[':
            stack.append(p)

        elif p == ')':
            if not stack:
                print('0')
                return

            if stack.pop() != '(':
                print('0')
                return
            else:
                depth[len(stack)] = 2
                if D[len(stack)+1] != 0:
                    depth[len(stack)] *= D[len(stack)+1]
                D[len(stack)+1] =  0
                D[len(stack)] += depth[len(stack)]
                depth[len(stack)] = 0
                
        else:
            if not stack:
                print('0')
                return

            if stack.pop() != '[':
                print('0')
                return
            else:
                depth[len(stack)] = 3
                if D[len(stack)+1] != 0:
                    depth[len(stack)] *= D[len(stack)+1]
                D[len(stack)+1] = 0
                D[len(stack)] += depth[len(stack)]
                depth[len(stack)] = 0
                
    print(f'{D[0]}')

solution()
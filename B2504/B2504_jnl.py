#괄호의 값
from calendar import c
import sys
input = sys.stdin.readline
print = sys.stdout.write

class Stack:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    class Index(Exception):
        pass
    class Iterate(Exception):
        pass

    def __init__(self, capacity:int=30):
        self.capacity = capacity
        self.stk = [None]*capacity
        self.ptr = 0
        self.iptr = 0

    def is_empty(self)->bool:
        return self.ptr <= 0

    def is_full(self)->bool:
        return self.ptr >= self.capacity

    def __len__(self)->int:
        return self.ptr
    
    def push(self, value:int)->None:
        if self.is_full():
            raise Stack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> int:
        if self.is_empty():
            raise Stack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def setValue(self, idx:int, value:int) -> None:
        if idx<0 or idx>self.capacity:
            raise Stack.Index
        self.stk[idx] = value
    
    def getValue(self, idx:int) -> int:
        if idx<0 or idx> self.capacity:
            raise Stack.Index
        return self.stk[idx]

    def __next__(self):
        if self.iptr < self.ptr:
            self.iptr += 1
            return self.stk[self.iptr-1]
        raise StopIteration
    
    def __iter__(self):
        return self


def solution():
    inputString = input().rstrip()
    ps = Stack(len(inputString))
    for char in inputString:
        ps.push(char)

    if len(ps) % 2 !=0: 
        print('0')
        return 

    depth = Stack(len(inputString)//2 +1)
    D = Stack(len(inputString)//2 +1)
    for _ in range(len(inputString)//2 +1):
        depth.push(0)
        D.push(0)
    
    stack = Stack() # 여는 괄호 넣어주는 용도

    for p in ps:
        if p =='(' or p == '[':
            stack.push(p)

        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                print('0')
                return

            else:
                depth.setValue(len(stack), 2)
                if D.getValue(len(stack)+1) != 0:
                    tmp = depth.getValue(len(stack))*D.getValue(len(stack)+1)
                    depth.setValue(len(stack), tmp)
                
                D.setValue(len(stack)+1, 0)

                tmp = D.getValue(len(stack)) + depth.getValue(len(stack))
                D.setValue(len(stack), tmp)

                depth.setValue(len(stack), 0)
                
        else:
            if stack.is_empty() or stack.pop() != '[':
                print('0')
                return
            else:
                # depth[len(stack)] = 3
                # if D[len(stack)+1] != 0:
                #     depth[len(stack)] *= D[len(stack)+1]
                # D[len(stack)+1] = 0
                # D[len(stack)] += depth[len(stack)]
                # depth[len(stack)] = 0

                depth.setValue(len(stack), 3)
                if D.getValue(len(stack)+1) != 0:
                    tmp = depth.getValue(len(stack))*D.getValue(len(stack)+1)
                    depth.setValue(len(stack), tmp)
                D.setValue(len(stack)+1, 0)
                tmp = D.getValue(len(stack)) + depth.getValue(len(stack))
                D.setValue(len(stack), tmp)
                depth.setValue(len(stack), 0)
                
    print(f'{D.getValue(0)}')

solution()
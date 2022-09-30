#괄호
import sys
input = sys.stdin.readline
print = sys.stdout.write

class Stack:
    class Empty(Exception):
        pass
    def __init__(self, string):
        self.capacity = len(string)
        self.stk = list(string)
        self.ptr = len(string)

    def __len__(self):
        return self.capacity
    
    def is_empty(self) -> bool:
        return self.ptr == 0

    def pop(self) -> int:
        if self.is_empty():
            raise Stack.Empty
        else:
            self.ptr -= 1
            return self.stk[self.ptr]

N = int(input())
for _ in range(N):
    inputPS = input().rstrip()
    ps = Stack(inputPS)
    if len(inputPS) % 2 != 0:
        print('NO\n')
        continue
    else:
        notmatched = 0
        while not ps.is_empty():
            p = ps.pop()
            if p == ')':
                notmatched += 1
            else:
                if notmatched == 0:
                    print('NO\n')
                    break
                else:
                    notmatched -= 1
                    if notmatched == 0:
                        try:
                            p = ps.pop()
                            if p == '(':
                                print('NO\n')
                                break
                            else:
                                notmatched += 1
                        except Stack.Empty:
                            print('YES\n')
                        
    if notmatched > 0:
        print('NO\n')
        
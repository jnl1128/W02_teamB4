# 카드 정렬하기
# N이 꽤 크다보니 sort()로 정렬하면 시간초과 날 듯

class PriorityQueue():
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity:int=100000):
        self.capacity = capacity
        self.que = [None]*capacity
        self.ptr = 0
        self.no = 0
        self.iptr = 0

    def __next__(self):
        if self.iptr < self.ptr:
            self.iptr += 1
            return self.que[self.iptr-1]
        raise StopIteration
    
    def __iter__(self):
        return self

    def is_empty(self)-> bool:
        return self.no<=0

    def is_full(self)-> bool:
        return self.no >= self.capacity

    def __len__(self)-> int:
        return self.no

    def push(self, value:int)->None:
        self.que[self.ptr] = value
        child = self.ptr
        parent = (child - 1)//2
        while parent >= 0:
            if self.que[parent] > self.que[child]:
                self.que[parent], self.que[child] = self.que[child], self.que[parent]
            else:
                break
            child = parent
            parent = (child-1)//2
        self.ptr += 1
        self.no += 1

    def pop(self)->int:
        x = self.que[0]
        self.que[self.ptr-1], self.que[0] = self.que[0], self.que[self.ptr-1]
        self.ptr -= 1
        self.no -= 1
        parent = 0
        childL = parent*2 + 1
        while childL < self.ptr:
            child = 0
            if parent * 2 + 2 < self.ptr:
                childR = parent *2 +2
                if self.que[childL]<self.que[childR]:
                    child = childL
                else:
                    child = childR
            else:
                child = childL
            
            if self.que[parent] > self.que[child]:
                self.que[parent] , self.que[child] = self.que[child], self.que[parent]
            else:
                break
            
            parent = child
            childL = parent * 2 + 1
        return x
            
import sys
input = sys.stdin.readline
print = sys.stdout.write


def solution():
    N = int(input())
    arr = PriorityQueue(N)
    for _ in range(N):
        arr.push(int(input()))
    total = 0
    while len(arr) >= 2:
        one = arr.pop()
        two = arr.pop()
        total += one+two
        if len(arr) != 0:
            arr.push(one+two)
    print(f'{total}')
solution()
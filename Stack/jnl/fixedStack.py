from typing import Any

# 고정 길이 스택
# 스택에서 push, pop, peek 등의 모든 작업들은 ptr을 바탕으로 이루어진다.
# 따라서 스택의 배열 원소값을 변경할 필요가 없다.
class FixedStack:
    
    class Empty(Exception):
        # 비어 있는 스택에 pop() 또는 peek()을 할 때 필요한 예외 처리
        pass
    class Full(Exception):
        # 이미 가득 찬 스택에 push()를 할 때 필요한 예외 처리
        pass

    def __init__(self, capacity:int=256) -> None:
        # 스택 초기화
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        # 스택에 쌓여 있는 데이터 개수 반환
        return self.ptr

    def is_empty(self) -> bool:
        # 스택이 비어 있는지
        return self.ptr <= 0
        # ==가 아니라 <=로 설정하면
            # 스택 배열의 최솟값과 최댓값에서 벗어나 접근하는 것을 막을 수 있음

    def is_full(self) -> bool:
        # 스택이 가득 차 있는지
        return self.ptr >= self.capacity

    def push(self, value:Any) -> None:
        # 스택에 value를 push()
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        # 스택에서 꼭대기에 있는 데이터를 pop()
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        # 스택에서 꼭대기 에 있는 데이터를 peek() _ 읽어옴
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self) -> None:
        # 스택을 비움 # 데이터를 모두 지움
        self.ptr = 0


    def find(self, value:Any) -> Any:
        # 스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    
    def count(self, value:Any)-> int:
        # 스택에서 value의 개수를 반환
        cnt = 0
        for i in range(self.ptr -1, -1, -1):
            if self.stk[i] == value:
                cnt += 1
        return cnt
    
    def __contains__(self, value:Any) -> bool:
        return self.count(value) > 0

    def dump(self) -> None:
        # 스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력
        if self.is_empty():
            print('스택이 비어 있습니다.')
        print(self.stk[:self.ptr])

    

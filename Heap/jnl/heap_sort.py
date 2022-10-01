from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    def down_heap(a:MutableSequence, left:int, right:int)->None:

        temp = a[left] #루트 # 값
        parent = left # 인덱스
        while parent < (right+1)//2:
            cl = parent * 2 + 1
            cr = cl + 1

            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child

        a[parent] = temp
    
    n = len(a)

    # a[i] ~ a[n-1]을 힙으로 만들기
    for i in range((n-1)//2, -1, -1):
        down_heap(a, i, n-1)
    
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0] # 최댓값인 a[0]와 마지막 원소를 교환
        down_heap(a, 0, i-1) # a[0] ~ a[i-1]을 힙으로 만들기



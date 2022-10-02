import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n = int(input())
arr= [None] #배열의 루트노드를 1로 하면 계산하기가 편해져서 arr[0]에는 쓰레기값을 하나 넣어놓음 

def do_push(num):
    arr.append(num)
    if len(arr)>2: 
        # 방금 append한 값의 인덱스를 i로 두고, 부모와 비교
        i = len(arr)-1 
        parent_i = i//2 # 부모 인덱스 
        
        # 위로 올라가면서 힙을 만든다
        # 맥스 힙은 항상 부모가 커야 하므로, 부모가 방금 자식보다 작은 한 계속해서 올라간다. 
        while arr[parent_i] < arr[i]:
                # 부모 < 자식이면
                temp = arr[i]
                arr[i] = arr[parent_i]
                arr[parent_i]= temp
                # i를 부모노드 인덱스로 바꾸고 다시 검색 
                i = parent_i
                parent_i = i//2 # 부모 인덱스 
                if parent_i<= 0:
                    break

def do_remove():
    if len(arr) ==1 :
        print(0)
    elif len(arr) ==2 :
        print(arr[1])
        del arr[1]
    else: 
        print(arr[1]) #가장 큰 값 출력
        arr[1]= arr[len(arr)-1] # 마지막 노드 값을 루트 노드에 저장 (배열 0번 인덱스 삭제하면 시간 오래 걸림)
        del arr[len(arr)-1] # 그리고 마지막 노드를 삭제하면 루트 노드를 삭제한 것과 동일한 결과
        i = 1
        # 밑으로 내려가면서 힙을 만든다
        while True :
            comparison =[arr[i]] # 비교할 세 값 (부모노드를 넣어놓고 시작 )
            if 2*i <= len(arr)-1 : # 왼쪽 자식 노드가 존재하면 
                comparison.append(arr[2*i])
                if 2*i +1 <= len(arr)-1 :  # 오른쪽 자식 노드도 존재하면 
                    comparison.append(arr[2*i+1])
            else: 
                # 왼쪽 자식 노드가 없으면 오른쪽도 없음 (즉 자식노드가 없다) -> 힙 상태
                break 
            
            # 세 값 중 최댓값의 인덱스를 반환 
            max_node = comparison.index(max(comparison))
            if max_node == 0: # 부모노드가 가장 크다 -> 힙 상태
                break
            elif max_node ==1: # 왼쪽 자식노드가 가장 크다 -> swap 
                temp = arr[i]
                arr[i] = arr[2*i]
                arr[2*i] = temp    
                i = 2*i
            else : # 오른쪽 자식노드가 가장 크다 -> swap 
                temp = arr[i]
                arr[i] = arr[2*i+1]
                arr[2*i+1] = temp  
                i = 2*i +1

for i in range(n):
    num = int(input())
    if num>0 :
        do_push(num)
    else: 
        do_remove()

        
# 145
# 1004
# 998
# 902
# 283
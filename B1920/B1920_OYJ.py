import sys
sys.stdin = open("/Users/yoojin/Desktop/python_practice/week02/input.txt","r")

n= int(sys.stdin.readline())
n_list = sorted(list(map(int,sys.stdin.readline().split())))
m= int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))


for a in m_list :
    min_index= 0
    max_index = n-1
    while min_index <= max_index:
        mid = (max_index+min_index)//2
        if a == n_list[mid] :
            print("1")
            break
        elif a < n_list[mid]:
            max_index = mid - 1
        else: 
            min_index = mid + 1
    if a != n_list[mid] :
        print("0")
 
 
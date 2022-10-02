import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n = int(input())
arr  = list(map(int,input().split()))
arr.sort()

temp = [2000000000,0,0] # 가능한 결과의 최댓값과 그때의 인덱스 두 개 
start = 0
end = len(arr)-1
while True:
    check_value = arr[start]+ arr[end]
    if abs(check_value) < temp[0] :
        temp[0] = abs(check_value)
        temp[1] = start
        temp[2] = end
    if check_value <0 :
        start += 1
    elif check_value ==0 :
        break
    else: 
        end -= 1
    if start>=end:
        break
print(arr[temp[1]], arr[temp[2]])
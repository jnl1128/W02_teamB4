import sys
sys.stdin = open("input.txt","r")

n= int(sys.stdin.readline())
count = {0:0,1:0}
square = []
for i in range(n):
    square.extend(list(map(int,sys.stdin.readline().split())))


def divide_and_conqure(n, square):
    upper_left_square = []
    upper_right_square = []
    lower_left_square = []
    lower_right_square = []
    if n ==1 :
        count[square[0]] += 1 
        return count
    # 정사각형 내 모든 요소의 min과 max이 같으면 (모두 0이거나, 모두 1이면) 멈추고, 다르면 나눈다
    elif min(square) == max(square) :
        # square의 첫번째 요소가 0 이면 count의 key 0의 value를 1 증가시키고, 1이면 1의 value를 1증가 시킨다.
        count[square[0]] += 1 
        return count
    else :
        for i in range(n//2):
            upper_left_square.extend(square[0:n//2])
            upper_right_square.extend(square[n//2:n])
            del square[0:n]
        for i in range(n//2):
            lower_left_square.extend(square[0:n//2])
            lower_right_square.extend(square[n//2:n])
            del square[0:n]
    
    # 각각의 사각형에 대해서 같은 작업 실행 
    divide_and_conqure(n//2, upper_left_square)
    divide_and_conqure(n//2, upper_right_square)
    divide_and_conqure(n//2, lower_left_square)
    divide_and_conqure(n//2, lower_right_square)

divide_and_conqure(n, square)

print(count[0])
print(count[1])
import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

# 기본적으로 나무자르기 문제와 같은 개념. (잘라야 하는 나무의 양 = 레벨 업해야 하는 총량)
# 레벨업하는 총량이 올릴 수 있는 레벨의 총합(k)을 넘어가지 않는 선에서 최대 높이를 찾는다. 
# 어차피 남는 레벨을 다 써도 min(Xn)은 똑같을 것 

def get_t_value () :  
    # 입력값 받기
    levels = []
    n, k = map(int,input().split())
    for i in range(n):
        levels.append(int(input()))
    # 시간초과가 떠서 먼저 sorted 시행 
    levels = sorted(levels)

    # 최저점은 가장 낮은 레벨(min(levels), 최고점은 k로 잡고, 이 둘의 평균을 t_value로 잡아서 이분탐색을 시작 
    lowest = min(levels)
    highest = max(levels) + k//n
    while lowest <= highest : 
        t_value = (lowest + highest)//2
        # total 변수는 현재의 t_value일 때 level up된 총량을 저장한다
        total = 0
        for level in levels:
            if t_value > level :
                total += t_value - level 
            else : 
                break 
        if total > k : # total 값이 k를 초과한다면 t_value를 낮춰야 함 
            highest = t_value -1
        elif total == k : ## total값이 k와 동일하다면 더이상 올릴 수 없음 
            return t_value 
        else : # total 값이 k 이하라면 t_value를 더 올릴 수 있음 
            temp = t_value 
            lowest = t_value +1 
    return temp
 
t = get_t_value()
print(t)

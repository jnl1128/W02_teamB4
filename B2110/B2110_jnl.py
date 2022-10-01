# 다른 코드 참조함
# 공유기 설치
import sys
input = sys.stdin.readline
print = sys.stdout.write

def solution():
    N, C = map(int, input().split(' '))
    homes = []
    for _ in range(N):
        homes.append(int(input()))
    homes.sort()

    # 공유기가 2개밖에 없다면 첫 번째 집과 마지막 집에 두면 끝남
    if C == 2:
        print(f'{homes[-1] - homes[0]}')
        return

    start = 1 #최소 간격(어차피 간격은 1이상일테니까)
    end = homes[-1] - homes[0] #최대 간격

    # mid: 현재 내가 선택한 거리
    while start < end:
        mid = (start + end)//2
        cnt = 1
        before = homes[0]
        for home in homes:
            if home-before >= mid:
                before = home
                cnt+= 1
        # if cnt == C로 따로 두게 되면 더 길게 할 수 있는 상황을 배제하게 됨
        if cnt >= C: 
            result = mid
            # 거리가 너무 짧다
            # 거리를 늘리자
            # start = mid +1 해주면 적어도 (start+end)//2의 결과로 이전의 mid보다는 커짐
            start = mid + 1
        else:
            # 거리가 너무 넓다
            # 거리를 좁히자
            # start = mid 해주면 적어도 (start+end)//2의 결과로 이전의 mid보다는 작아짐
            end = mid

    print(f'{result}')
    return 

solution()   
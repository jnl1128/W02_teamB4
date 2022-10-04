import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n,c = map(int,input().split())
houses = []
for i in range(n):
    houses.append(int(input()))
houses.sort()

possibleAnswer = 0 

minGap, maxGap = 1,houses[-1]- houses[0]
while True: 
    wifi = houses[0] # wifi 변수에는 가장 마지막으로 와이파이를 설치한 집의 좌표를 저장한다. 
    count= 1
    midGap = (minGap + maxGap)//2
    # 설정한 midGap으로 공유기를 설치해본다
    for i in range(1, n):
        if houses[i] - wifi >= midGap:
            count += 1
            wifi = houses[i]

    # 설치한 공유기의 갯수를 토대로, 범위를 조정한다
    if count >= c: #공유기 갯수가 필요한 양보다 많거나 같으면 간격을 높인다 
        possibleAnswer = midGap
        minGap = midGap +1 
    else : # #공유기 갯수가 필요한 갯수보다 부족하면 간격을 줄인다
        maxGap = midGap -1
    if minGap > maxGap :
        break 

print(possibleAnswer)
    

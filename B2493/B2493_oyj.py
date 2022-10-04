import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

# 입력 받기
n = int(input())
arrN = list(map(int,input().split()))
answer= []

sendPtr = 0 # sendPtr = 기준이 되는 요소의 인덱스 (송신하는 탑) 첫 탑부터 시작
for i in range(n): #요소의 갯수 만큼 반복
    #arrN[sendPtr]를 temp 변수에 임시로 저장
    temp = arrN[sendPtr]
    # receivedPtr = 수신하는 탑의 인덱스. sendPtr 이전 인덱스부터 arrN을 탐색 
    receivePtr = sendPtr - 1   

    while True:  
        # receivePtr< 0 이 되면 0을 출력하고 반복문을 빠져나온다. 
        if receivePtr < 0 : 
            answer.append(0)
            break
       # receivePtr의 원소 값이 temp보다 같거나 크면, 해당 값을 출력하고. 빠져나온다 -> Break 
        elif arrN[receivePtr] >= temp : 
            answer.append(receivePtr+1)
            break
        else:  # ptr의 원소값이 temp 보다 작으면 ptr의 answer를 확인하고, 해당 값으로 ptr를 이동한다. 
            if answer[receivePtr]== 0:
                answer.append(0)
                break
            else:
                receivePtr = answer[receivePtr] -1 # 확인 
    sendPtr +=1 

print(*answer)


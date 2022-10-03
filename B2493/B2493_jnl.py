#탑 # 탑의 높이는 다 다르다
import sys
input = sys.stdin.readline
print = sys.stdout.write

def solution():
    N = int(input())
    arr = list(map(int,input().split(' ')))
    
    tallest = [0]
    print('0 ')
    for i in range(1, N):
        # 내가 바로 전꺼보다 크더라고
        if arr[i] > arr[i-1]:
            flag = True
            while tallest:
                t = tallest.pop()
                if arr[i] < arr[t]:
                    tallest.append(t)
                    break
            if len(tallest) == 0:
                flag = False
            if flag: # 나보다 큰 애가 있더라고
                print(f'{tallest[-1]+1} ')
            else: # 나보다 큰애가 없더라고
                print('0 ')
            # 일단 내가 바로 전꺼보다 크니까 넣어볼게
            tallest.append(i)

        # 내가 바로 전꺼보다 작더라고
        else:
            tallest.append(i-1)
            print(f'{i} ')

solution()

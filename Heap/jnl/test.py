N = int(input())
que = []
for _ in range(N):
    num = int(input())
    if not que:
        que.append(num)
    else:
        que.append(num) #[1,2]
        idx = len(que)-1 # 1
        while que[(idx-1)//2] < que[idx]:
            print('swap')
            que[(idx-1)//2], que[idx] =  que[idx], que[(idx-1)//2]
            idx = (idx-1)//2
            if idx <= 0:
                break
    print(que)
        





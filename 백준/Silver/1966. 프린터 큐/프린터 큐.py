from collections import deque

T = int(input())

for _ in range(1, T+1):
    n, m = map(int, input().split())
    file = deque(list(map(int, input().split())))
    idx = deque([i for i in range(len(file))])
    point = file[m]
    cnt = 0 
    while True:
        max_val = max(file)
        if file[0] != max(file):
            a = file.popleft()
            file.append(a)
            b = idx.popleft()
            idx.append(b)
        elif file[0] == max(file):
            if file[0] == point and idx[0] == m:
                cnt += 1
                break
            file.popleft()
            idx.popleft()
            cnt += 1
    print(cnt)
from collections import deque

for _ in range(int(input())):
    com = input()
    n = int(input())
    lst = input()[1:-1].split(',')
    cnt = 0
    Q = deque(lst)

    if not n:
        Q = []
    for i in com:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if not len(Q):
                print('error')
                break
            else:
                if not (cnt % 2):
                    Q.popleft()
                else:
                    Q.pop()
    else:
        if not (cnt%2):
            print("[" + ",".join(Q) + "]")
        else:
            Q.reverse()
            print("[" + ",".join(Q) + "]")
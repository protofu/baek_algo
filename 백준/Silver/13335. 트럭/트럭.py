N, W, L = map(int, input().split()) # 트럭수, 다리 길이, 다리 하중
truck = list(map(int, input().split()))
Q = [0] * W
time = 0
while Q:
    time += 1
    Q.pop(0)
    if truck:
        if sum(Q) + truck[0] > L:
            Q.append(0)
        else:
            Q.append(truck.pop(0))

print(time)
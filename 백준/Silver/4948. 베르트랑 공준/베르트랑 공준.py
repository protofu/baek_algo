era = [0, 0] + [1 for _ in range(2*123456)]
for i in range(2, int((2*123456)**0.5)):
    for j in range(i+i, len(era), i):
        era[j] = 0

while True:
    num = int(input())
    if num == 0:
        break
    print(sum(era[num+1:2*num+1]))
        
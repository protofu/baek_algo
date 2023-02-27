Sum = flag = 0
for _ in range(10):
    if not flag:
        score = int(input())
        Sum += score

        if Sum >= 100:
            flag = 1
    else:
        throw = int(input())
if Sum-100 > abs(Sum - score - 100):
    print(Sum-score)
else:
    print(Sum)
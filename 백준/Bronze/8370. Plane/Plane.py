rlt = list(map(int, input().split()))
ans = 0
for i in range(0, 4, 2):
    ans += (rlt[i]*rlt[i+1])
print(ans)
import sys
input = sys.stdin.readline

n = int(input())
arr = []
# 에라토스테네스의 체
a = [False,False] + [True]*(n-1)
for i in range(2,int(n**0.5)+1):
    if a[i]:
        a[i*2::i] = [False]*((n-i)//i)

# 소수 배열 생성
for i in range(n+1):
    if a[i] == True:
        arr.append(i)

cnt,summ = 0,0
i,j = 0,0
while(True):
    if summ == n:
        cnt+=1
        
    if summ > n:
        summ -= arr[i]
        i+=1
    elif j == len(arr):
        break
    else:
        summ += arr[j]
        j+=1
        
print(cnt)
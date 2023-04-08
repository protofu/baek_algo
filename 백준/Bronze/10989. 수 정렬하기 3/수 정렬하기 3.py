import sys

T=int(input())
num_list=[0]*10001
for _ in range(T):
    a=int(sys.stdin.readline())
    num_list[a]+=1
for i in range(1,10001):
    for _ in range(num_list[i]):
        print(i)
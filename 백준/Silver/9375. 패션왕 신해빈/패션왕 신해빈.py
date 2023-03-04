import sys
input = sys.stdin.readline

for tc in range(int(input())):
    dic = {}
    ans = 1
    n = int(input())
    for _ in range(n):
         typ = list(input().split())
         if typ[1] not in dic:
             dic[typ[1]] = 1
         else:
             dic[typ[1]] += 1
    for i in dic.values():
        ans *= i+1

    print(ans-1)
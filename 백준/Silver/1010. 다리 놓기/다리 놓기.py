import sys

def fac(num): # 펙토리얼 재귀 함수 구현
    if num <= 1:
        return 1
    return fac(num-1) * num

n = int(input())    # test_case 받고
for _ in range(n):
    L, R = map(int, sys.stdin.readline().split())   #왼쪽 오른쪽 사이트 받고

    bri_case = fac(R) // (fac(R-L) * fac(L)) # 조합론에 의한 식

    print(bri_case)
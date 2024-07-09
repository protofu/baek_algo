T = int(input())

for _ in range(T):
    h, r, g = map(int, input().split())
    n = g//h+1
    hi= g%h
    if g%h==0:
        n=g//h
        hi= h
    print(hi*100+n)
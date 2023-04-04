while True:
    a = int(input())
    ans = 0
    if not a:
        break
    else:
        for i in range(1, a+1):
           ans += i
    print(ans)
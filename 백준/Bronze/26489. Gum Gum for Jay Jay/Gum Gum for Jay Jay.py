cnt = 0
while True:
    try:
        lst = list(input().split())
        cnt+=1
    except EOFError:
        print(cnt)
        break
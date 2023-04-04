i = 1
while True:
    lst = list(map(int, input().split()))
    if not lst[-1]:
        break
    print(f'Case {i}: Sorting... done!')
    i += 1

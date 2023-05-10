for _ in range(int(input())):
    d, n = map(int, input().split())
    numbers = list(map(lambda x: int(x)%d, input().split())) # 0, 1, 2, 3 으로
    ans = 0
    visited = [1] + [0] * 1000000
    for num in numbers:
        ans = (ans + num) % d
        visited[ans] += 1
    result = 0
    for i in range(d):
         result += visited[i] * (visited[i] - 1) // 2
    print(result)
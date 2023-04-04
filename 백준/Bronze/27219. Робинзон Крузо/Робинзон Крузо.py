n = int(input())
for _ in range(n//5):
    print('V', end='')
for _ in range(n%5):
    print('I', end='')
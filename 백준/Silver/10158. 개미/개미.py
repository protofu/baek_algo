w, h = map(int, input().split())
x, y = map(int, input().split())
time = int(input())
x_len = (x + time) // w
y_len = (y + time) // h

if y_len % 2:
    y = h - (y + time) % h
else:
    y = (y + time) % h

if x_len % 2:
    x = w - (x + time) % w
else:
    x = (x + time) % w

print(x, y)
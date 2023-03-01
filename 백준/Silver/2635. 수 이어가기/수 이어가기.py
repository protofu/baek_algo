n = int(input())
l = 0
for two in range(1, n+1):
    num_lst = [n, two]
    while True:
        if num_lst[-2] - num_lst[-1] < 0:
            break
        else:
            num_lst.append(num_lst[-2] - num_lst[-1])
    if len(num_lst) > l:
        l = len(num_lst)
        ans_two = two
num_lst = [n, ans_two]
while True:
    if num_lst[-2] - num_lst[-1] < 0:
        break
    else:
        num_lst.append(num_lst[-2] - num_lst[-1])
        
print(len(num_lst))
print(*num_lst)
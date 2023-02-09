T = int(input())
num_list =[]
for _ in range(T):
    num_list.append(int(input()))

num_list.sort()

for i in num_list:
    print(i)
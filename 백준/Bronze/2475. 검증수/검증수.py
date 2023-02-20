num = map(int, input().split())

nums = map(lambda n:n*n,num)

rlt = sum(nums)

a=rlt%10

print(a)
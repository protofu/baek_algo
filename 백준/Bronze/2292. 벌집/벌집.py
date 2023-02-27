N=int(input())
n=N
i=0
if N==1:
        print('1')

else:
    n-=1
    while True:
        i+=1
        n-=(6*i)
        if n<=0:
            print(i+1)
            break
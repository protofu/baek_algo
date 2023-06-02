s,k,h=map(int,input('').split())

sum=s+k+h

if sum>=100:
    print('OK')
else:
    min_num=min(s,k,h)
    if s==min_num:
        print('Soongsil')
    if k==min_num:
        print('Korea')
    if h==min_num:
        print('Hanyang')
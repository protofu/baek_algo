import sys

def solution(tri):
    tmp = []
    while tri:
        rlt = tri.pop()
        if tmp:
            for i in range(len(rlt)):
                rlt[i] += tmp[i]
            tmp = []
        for i in range(len(rlt)-1):
            tmp.append(max(rlt[i:i+2]))
    
    return rlt[0]
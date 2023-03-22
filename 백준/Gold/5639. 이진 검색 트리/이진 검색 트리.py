import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

node = []
while True:
    try:
        N = int(input())
        node.append(N)
    except:
        break

def binary(S, E):
    if S > E:
        pass
    else:
        m = E + 1
        for i in range(S+1, E+1):
            if node[S] < node[i]:
                m = i
                break
        binary(S+1, m-1)
        binary(m,E)
        print(node[S])
binary(0, len(node)-1)
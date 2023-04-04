import sys
sys.setrecursionlimit(10**6)

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return

    root = postorder[postEnd]

    leftNode = nodes[root] - inStart
    rightNode = inEnd - nodes[root]

    print(root, end=" ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
nodes = [0] * (n+1)

for i in range(n):
    nodes[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)
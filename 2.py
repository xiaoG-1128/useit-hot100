def dfs(node,father):
    traversal_result.append(node)
    for child in adjList[node]:
        if child != father:
            dfs(child,node)
n=int(input())
tree_type=int(input())

adjList=[[] for _ in range(n+1)]
traversal_result=[]

if tree_type == 1:
    for _ in range(n-1):
        u,v=map(int,input().split())
        adjList[u].append(v)
        adjList[v].append(u)
elif tree_type == 2:
    father = list(map(int,input().split()))
    for i in range(1,n+1):
        if father[i-1]!=0:
            adjList[father[i-1]].append(i)
            adjList[father[i]].append(i-1)

for i in range(1,n+1):
    adjList[i].sort()

dfs(1,0)

print(" ".join(map(str,traversal_result)))
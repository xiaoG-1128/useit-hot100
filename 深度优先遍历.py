from asyncio import gather


def dfs(node,father):
    traversal_result.append(node)
    for child in adjList[node]:
        if child != father:
            dfs(child,node)

n = int(input())
tree_type = int(input())

adjList = [[] for _ in range(n+1)] #邻接表
traversal_result = [] #存储遍历结果

if tree_type == 1:
    for _ in range(n-1):
        u,v = map(int,input().split())
        adjList[u].append(v)
        adjList[v].append(u)
elif tree_type == 2:
    father = list(map(int,input().split()))
    for i in range(1,n+1):
        if father[i-1]!= 0:
            adjList[father[i-1]].append(i)

for i in range(1,n+1):
    adjList[i].sort()  #针对int类型，sort默认为从小到大

dfs(1,0)

print(" ".join(map(str,traversal_result)))

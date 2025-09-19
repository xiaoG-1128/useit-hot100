n=int(input())

adj_a={i:[] for i in range(n+1)}
for i in range(1,n+1):
    row = list(map(int,input().split()))
    for j in range(i,n+1):
        if row[j-1]==1:
            adj_a[i].append(j)
adj_b=[[]for _ in range(n+1)]
for _ in range(n):
    data = list(map(int,input().split()))
    node = data[0]
    k= data[1]
    neighbors = data[2:]
    adj_b[node].extend(neighbors)

for i in range(1,n+1):
    adj_a[i].sort()
    adj_b[i].sort()

same = True

for i in range(1,n+1):
    if adj_a[i]!=adj_b[i]:
        same = False
        break

print("YES" if same else "NO")



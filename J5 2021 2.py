M = int(input())
N = int(input())
K = int(input())

grid = [[False for j in range(N)] for i in range(M)]

r = [False for i in range(N)]
c = [False for i in range(M)]

for i in range(K):
    a, b = input().split()
    b = int(b)-1
    if a == 'R':
        r[b] = not r[b]
    if a == 'C':
        c[b] = not c[b]

for i in range(N):
    if r[i]:
        for j in range(N):
            grid[i][j] = not grid[i][j]
for i in range(M):
    if c[i]:
        for j in range(M):
            grid[j][i] = not grid[j][i]

count = 0
for i in range(M):
    count += grid[i].count(True)

print(count)

M = int(input())
N = int(input())
K = int(input())

grid = [[False for j in range(N)] for i in range(M)]

for i in range(K):
    a, b = input().split()
    b = int(b)-1
    if a == "R":
        for j in range(N):
            grid[b][j] = not grid[b][j]
    if a == "C":
        for j in range(M):
            grid[j][b] = not grid[j][b]

count = 0
for i in range(M):
    count += grid[i].count(True)

print(count)


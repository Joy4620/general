M = int(input())
N = int(input())
success = ['no']

table = []

for i in range(M):
    table.append(list(map(int, input().split())))

def check(row, col):
    if row >= M or col >= N or table[row][col] == 0:
        return
    if row == M-1 and col == N-1:
        success[0] = 'yes'
        return
    
    current = table[row][col]
    table[row][col] = 0

    for i in range(1, current):
        if current % i == 0:
            check(i-1, (current//i)-1)

check(0, 0)
print(success[0])

M = 3
N = 4
success = ['no']

table = [[3, 10,  8, 14],
         [1, 11, 12, 12],
         [6,  2,  3,  9]]


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
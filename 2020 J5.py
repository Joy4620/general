#input:
'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9
'''
#output:
'''
yes
'''
# row = 3
# column = 4
# grid=[[3, 10, 6, 14],
#       [1, 11, 12, 12],
#       [3, 2, 3, 9]]

row = int(input())
column = int(input())
grid = [[int(j) for j in input().split()] for i in range(row)]

stack = [grid[0][0]]
visited = []


def factors(current):
    global row
    global column
    for rowNumber in range(1, min(current, row) + 1):
        if current % rowNumber == 0:
            if current//rowNumber <= column:
                add = grid[rowNumber-1][(current//rowNumber)-1]
                if add not in visited and add not in stack:
                    stack.append(add)


while stack:
    current = stack.pop(0)
    visited.append(current)
    if current == row * column:
        print('yes')
        break
    factors(current)
else:
    print('no')


'''
plan: use recursion with a list
starting on list[0][0]
if on list[M][N], then output 'yes', otherwise, output no once
a certain limit is reached

recursion:
- start on current
- find factors of current
- go to that place and mark current (eg. current = list[f1][f2])
- other recurses go to different places (e.g. list[f2][f1])

how to find dead end?
- when current goes on a number already visited, end that specific loop

how to find all factors of a number?
- if statements and modulation; variable to len(num)
  - if factor(s) bigger than M/N (depending on which factor), skip that
- variable to keep track of factors done (e.g. done 1, so recurse, next loop is variable + 1)

what happens if current is in visited? do we have to recurse with a different bookmark?

what happens if factors are found, but there are other factors, but recurse is now at different number?

I don't think bookmark is working. I've been using it when the num could be a totally different number
- I should use it when num is the same number, but how?
- Bookmark is useless with a different number. It shouldn't even be used

can recursion be used twice in one function?


pseudocode:
- set grid
- set current (a list [x, y])
- set factor bookmark (1)
- set places visited

- recursion(bookmark, current)
    - if current = [M-1, N-1: return 'yes']
    - if current in visited: pass

    - # This is to find factor and go there
    - for i in range(bookmark, len(num)): if num%i == 0, if (i <= M and num/i <= N) or (i <= N and num/i <= M): current = [i, num/i],\
        bookmark = i, visited += [current], recursion(bookmark, current)


'''

# M = 3
# N = 4

# grid = [[3, 10,  8, 14],
#         [1, 11, 12, 12],
#         [6,  2,  3,  9]]

# current = [0, 0]
# bookmark = 1
# visited = []

# def recursion(bookmark, current):
#     global visited
#     global grid
#     global M
#     global N
#     print(f'Current {current}, bookmark {bookmark}, visited {visited}')
#     if current == [M-1, N-1]:
#         return "yes"
#     if current in visited:
#         print('current in visited')
#         recursion(bookmark, current)
#     num = int(grid[current[0]][current[1]])
#     for i in range(bookmark, num):
#         if num%i == 0:
#             if i <= M and num/i <= N:
#                 recursion(bookmark, current)
#                 current = [i, num/i]
#                 bookmark += i
#                 visited += current
#                 recursion(bookmark, current)
#             # if (i <= M and num/i <= N) or (i <= N and num/i <= M):
#             #     if i <= M and num/i <= N:
#             #         current = [i, num/i]
#             #     elif i <= N and num/i <= M:
#             #         current = [num/i, i]
#             #     bookmark = i


# recursion(bookmark, current)


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


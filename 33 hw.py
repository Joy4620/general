Matrix = [
    ['w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', '.', 'w', 'w', 'w'],
    ['w', '.', '.', 'w', 'w', 'w'],
    ['w', '.', '.', '.', 'w', 'w'],
    ['w', 'S', 'w', 'A', '.', 'w'],
    ['w', '.', 'w', 'w', 'w', 'w'],
    ['w', '.', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', '.', '.', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w'],
]

current = 0

# bps
print('bps')
stack = [(4, 1)]
while stack:
    x, y = stack.pop(0)
    # print(stack)
    if Matrix[x][y] not in 'w0123456789A':
        Matrix[x][y] = str(current)
        current += 1
        stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
for i in Matrix:
    print(i)


# dps
print('dps')
stack = [(4, 1)]
while stack:
    x, y = stack.pop()
    # print(stack)
    if Matrix[x][y] not in 'w0123456789A':
        Matrix[x][y] = str(current)
        current += 1
        stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
for i in Matrix:
    print(i)

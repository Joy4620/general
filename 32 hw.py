# floodfill
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

# recursion
def f(x, y):
    if Matrix[x][y] in 'w0A':
        return
    Matrix[x][y] = 0
    f(x-1, y)
    f(x+1, y)
    f(x, y-1)
    f(x, y+1)

f(4, 1)
for i in Matrix:
    print(i)


# iteration
Stack = [(4, 1)]
while Stack:
    x, y = Stack.pop(0)
    if Matrix[x][y] not in 'w0A':
        Matrix[x][y] = '0'
        Stack.append((x-1, y))
        Stack.append((x+1, y))
        Stack.append((x, y+1))
        Stack.append((x, y-1))


# fibonacci
# recursion
def f(n):
    if n == 0 or n == 1: 
        return n
    return f(n-1)+f(n-2)


# iteration
a = 0
b = 1
for i in range(10):
    a, b = b, b + a
    print(a)




class Floodfill:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
node = Floodfill(4, 1)
stack = [node]
visited = ['w', 'A']
current = 0

while stack:
    P = stack.pop(0)
    if Matrix[P.x][P.y] not in visited:
        Matrix[P.x][P.y] = str(current)
        visited.append(str(current))
        current += 1
        stack.extend([(P.x-1, P.y), (P.x+1, P.y), (P.x, P.y-1), (P.x, P.y+1)])
for i in Matrix:
    print(i)


# print(node.x)
# P = stack[0]
# print(type(P.x))
# print(Matrix[P.x][P.y] in 'S')
# print(P.x-1)
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.steps = 0
#     def bark(self):
#         print(self.name, 'bark!')

# hehe = Dog('hrfud')
# hehe.bark()

# Stack = [(4, 1)]
# while Stack:
#     x, y = Stack.pop(0)
#     if Matrix[x][y] not in 'w0A':
#         Matrix[x][y] = '0'
#         Stack.append((x-1, y))
#         Stack.append((x+1, y))
#         Stack.append((x, y+1))
#         Stack.append((x, y-1))

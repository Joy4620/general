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
    P = stack.pop()
    print(Matrix[P.x][P.y])
    if Matrix[P.x][P.y] not in visited:
        Matrix[P.x][P.y] = str(current)
        visited.append(str(current))
        current += 1
        stack.extend([Floodfill(P.x-1, P.y), Floodfill(P.x+1, P.y), Floodfill(P.x, P.y-1), Floodfill(P.x, P.y+1)])
        # stack.extend([object1，object2，object3, object4])
for i in Matrix:
    print(i)

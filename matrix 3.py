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


def replace(row, column):
    if Matrix[row][column] in 'w0':
        return

    if Matrix[row][column] == '.':
        Matrix[row][column] = '0'

    replace(row-1, column)
    replace(row+1, column)
    replace(row, column+1)
    replace(row, column-1)


replace(4, 1)

for i in range(len(Matrix)):
    print(Matrix[i])

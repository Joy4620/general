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


# start at S
# options: up down left right
# if one of those is ., make it into 0
# otherwise, stop current recurse
# base: 
# if there isn't '.' in Matrix, break

times = 0


def replace(row, column, message):
    global times
    print('beginning of one round')
    print(message)
    # if row > 10 or column > 10 or row < 0 or column < 0:
    #     print('row or column exceeds limit: ', row, column)
    #     return
    if times > 100:
        return
    # success = False
    # for i in range(len(Matrix)):
    #     for j in range(len(Matrix[0])):
    #         if Matrix[i][j] == '.':
    #             success = True
    # if success is False:
    #     return print('success is False')

    try:
        current = Matrix[row][column]
    except:
        print('current has error')
        return

    if current == 'w':
        print('current hit wall')
        return

    if current == '.':
        print('current replaced by 0')
        Matrix[row][column] = '0'
    print('one round')
    for j in range(len(Matrix)):
        print(Matrix[j])

    times += 1

    replace(row-1, column, 'up')
    replace(row+1, column, 'down')
    replace(row, column+1, 'right')
    replace(row, column-1, 'left')


replace(4, 1, None)

for i in range(len(Matrix)):
    print(Matrix[i])

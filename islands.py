Matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
]


def oneisland(x, y):
    if x > len(Matrix)-1 or x < 0 or y > len(Matrix[0])-1 or y < 0:
        return
    if Matrix[x][y] == 0:
        return
    elif Matrix[x][y] == 1:
        Matrix[x][y] = 2
        oneisland(x+1, y)
        oneisland(x-1, y)
        oneisland(x, y+1)
        oneisland(x, y-1)

def find1():
    for i in range(len(Matrix)):
        try:
            return (i, Matrix[i].index(1))
        except:
            continue
    return False

count = 0  # number of islands
while True:  # while there are still untouched islands left...
    try:
        x, y = find1()  # index for untouched island
        oneisland(x, y)  # fill the island up
        count += 1  # add one to # of islands total
    except:
        break  # all islands are explored

for i in Matrix:
    print(i)

print(count)

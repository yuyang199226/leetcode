

def print_array(numbers):
    rows = len(numbers)
    cols = len(numbers[0])
    start = 0
    while rows > 2 * start and cols > 2 * start :
        print_circle(start, rows, cols, numbers)
        start += 1


def print_circle(start, rows, cols, numbers):
    endx = cols - 1 - start
    endy = rows - 1 - start
    # 从左到右打印

    for i in range(start, endx+1):
        print(numbers[start][i])
    # 从上到下打印

    if endy > start:
        for i in range(start+1, endy+1):
            # print(endx,i)
            print(numbers[i][endx])
    # 从右到左
    if endy > start and endx > start:

        for i in range(endx-1, start-1, -1):
            # print(endy, i)
            print(numbers[endy][i])

    if endy-1 > start and endx > start:
        for i in range(endy-1, start, -1):
            print(numbers[i][start])


a1 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
a2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
a3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
print_array(a3)




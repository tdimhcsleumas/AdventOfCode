def enqueueMatrix(matrix):
    queue = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            queue.append((i, j))
    return queue


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        matrix = []
        for line in f.readlines():
            matrix.append([int(x) for x in line.strip()])

        flashedCount = 0
        
        for _ in range(100):
            eventQueue = enqueueMatrix(matrix)
            flashedSet = set()

            while len(eventQueue) != 0:
                (i, j) = eventQueue.pop(0)
                if (i, j) in flashedSet: continue

                if matrix[i][j] == 9:
                    matrix[i][j] = 0
                    flashedCount += 1
                    flashedSet.add((i, j))

                    # enqueue the surrounding nodes, but prepend them
                    coordsToEnqueue = [
                        (i-1,j-1),
                        (i-1,j),
                        (i-1,j+1),
                        (i,j-1),
                        (i,j+1),
                        (i+1,j-1),
                        (i+1,j),
                        (i+1,j+1)
                    ]
                    for (x, y) in coordsToEnqueue:
                        if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[x]):
                            eventQueue.append((x, y))
                else:
                    matrix[i][j] += 1

                # print(flashedSet)

        for row in matrix:
            print(row)

        print(flashedCount)
from collections import defaultdict

def makeVertexSet(matrix):
  vertexSet = set()
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      vertexSet.add((i,j))
  return vertexSet

def extractMin(vertexSet: set, dist: dict):
  min = None
  minVal = None
  for vertex in vertexSet:
    if not min or dist[vertex] < minVal:
      min = vertex
      minVal = dist[vertex]

  vertexSet.remove(min)
  return min

if __name__ == "__main__":
  with open("input.txt") as f:
    matrix = []
    for line in f.readlines():
      row = [int(x) for x in line.strip()]
      matrix.append(row)

    vertexSet = makeVertexSet(matrix)
    dist = defaultdict(lambda: float('inf')) # use absence from the set as INFINITY
    prev = {} # use absence from the set as UNDEFINED

    dist[(0,0)] = 0

    while len(vertexSet) != 0:
      (i, j) = extractMin(vertexSet, dist)

      # for each neighbor 
      neighbors = [
        (i, j+1),
        (i+1, j)
      ]
      for (x, y) in neighbors:
        if x > len(matrix) - 1 or y > len(matrix[i]) - 1: continue
        alt = dist[(i, j)] + matrix[x][y]

        if alt < dist[(x,y)]:
          dist[(x,y)] = alt
          prev[(x,y)] = (i,j)

    print(dist[(len(matrix) - 1, len(matrix[0]) - 1)])
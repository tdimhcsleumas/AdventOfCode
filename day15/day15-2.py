from heapq import heappush, heappop
import itertools
from heapdict import heapdict

def makeVertexSet(matrix):
  vertexSet = set()
  for i in range(len(matrix) * 5):
    for j in range(len(matrix[0]) * 5):
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

def getRisk(matrix, point):
  (x,y) = point
  baseVal = matrix[x % len(matrix)][y % len(matrix[0])] - 1

  dx = x // len(matrix)
  dy = y // len(matrix[0])

  return ((baseVal + dx + dy) % 9) + 1

if __name__ == "__main__":
  with open("input.txt") as f:
    matrix = []
    for line in f.readlines():
      row = [int(x) for x in line.strip()]
      matrix.append(row)

    vertexSet = makeVertexSet(matrix)
    dist = {} 
    hd = heapdict()

    for vertex in vertexSet:
      dist[vertex] = float('inf')
      hd[vertex] = dist[vertex]

    dist[(0,0)] = 0
    hd[(0,0)] = 0

    maxRow = (len(matrix) * 5) - 1
    maxCol = (len(matrix) * 5) - 1

    while len(hd) > 0:
      ((i, j), _) = hd.popitem()

      # for each neighbor 
      neighbors = [
        (i-1, j),
        (i, j+1),
        (i+1, j),
        (i, j-1)
      ]
      for (x, y) in neighbors:
        if x > maxRow or y > maxCol or x < 0 or y < 0: continue
        alt = dist[(i, j)] + getRisk(matrix, (x,y))

        if alt < dist[(x,y)]:
          dist[(x,y)] = alt
          hd[(x,y)] = alt

    print(dist[(maxRow, maxCol)])
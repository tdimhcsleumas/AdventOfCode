def calculatePoint(point, grid, algorithm, isOdd):
  (i,j) = point
  points = [
    (i-1,j-1),
    (i-1,j),
    (i-1,j+1),
    (i,j-1),
    (i,j),
    (i,j+1),
    (i+1,j-1),
    (i+1,j),
    (i+1,j+1)
  ]
  num = 0

  for (x,y) in points:
    num <<= 1
    if (x,y) in grid:
      num += grid[(x,y)] == '#'
    else:
      num += isOdd

  return algorithm[num]

if __name__ == "__main__":
  with open("input.txt") as f:
    lines = f.readlines()
    algorithm = lines[0]

    grid = dict()

    for i, line in enumerate(lines[2:]):
      for j, c in enumerate(line.strip()):
        if c == "#":
          grid[(i,j)] = '#'

    for x in range(50):
      newGrid = dict()
      processSet = set()

      for (i,j) in grid.keys():
        points = [
          (i-1,j-1),
          (i-1,j),
          (i-1,j+1),
          (i,j-1),
          (i,j),
          (i,j+1),
          (i+1,j-1),
          (i+1,j),
          (i+1,j+1)
        ]
        for point in points:
          processSet.add(point)

      for (i,j) in processSet:
        if calculatePoint((i,j), grid, algorithm, x % 2 != 0) == '#':
          newGrid[(i,j)] = '#'
        else:
          newGrid[(i,j)] = '.'
      
      grid = newGrid
      processSet.clear()

  print(len(newGrid.keys()))

  litCount = 0
  for item in newGrid.values():
    if item == "#":
      litCount += 1
  print(litCount)

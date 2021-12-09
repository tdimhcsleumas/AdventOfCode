from dataclasses import dataclass

@dataclass
class QueueEntry:
  row: int
  col: int
  basin: set


if __name__ == "__main__":
  filename = "input.txt" 
  with open(filename) as f:
    lines = f.readlines()
    map = []

    for idx, line in enumerate(lines):
      numLine = [int(x) for x in line.strip()]
      map.append(numLine)

    queue = []
    basins = []
    visited = {}
    for i in range(len(map)):
      for j in range(len(map[i])):
        if i > 0 and map[i-1][j] <= map[i][j]: continue
        if i < len(map) - 1 and map[i+1][j] <= map[i][j]: continue
        if j > 0 and map[i][j-1] <= map[i][j]: continue
        if j < len(map[i]) - 1 and map[i][j+1] <= map[i][j]: continue
        basin = set([(i, j, map[i][j])])
        basins.append(basin)
        queue.append((i, j, basin))

    # do a bfs starting with each of the low points
    while len(queue) != 0:
      (i, j, basin) = queue.pop(0)

      # union already discovered points
      if visited.get((i, j)):
        visited[(i, j)] |= basin
        basin |= visited[(i, j)]
        continue

      visited[(i, j)] = basin

      if i > 0 and map[i-1][j] != 9:
        queue.append((i-1, j, basin))
      if i < len(map) - 1 and map[i+1][j] != 9:
        queue.append((i+1, j, basin))
      if j > 0 and map[i][j-1] != 9:
        queue.append((i, j-1, basin))
      if j < len(map[i]) - 1 and map[i][j+1] != 9:
        queue.append((i, j+1, basin))

      basin.add((i, j, map[i][j]))

    sortedBasins = sorted(basins, key=lambda x: -1 * len(x))
    print(len(sortedBasins[0]) * len(sortedBasins[1]) * len(sortedBasins[2]))

        



 

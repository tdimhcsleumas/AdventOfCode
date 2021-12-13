from re import search

def foldGrid(grid: set, instruction: str):
  m = search("\w+ ([xy])=(\d+)", instruction)
  axis = m.group(1)
  value = int(m.group(2))
  newGrid = set()

  for (x, y) in grid:
    if axis == "x" and x > value:
      dx = x - value
      newGrid.add((value - dx, y))
    elif axis == "y" and y > value:
      dy = y - value
      newGrid.add((x, value - dy))
    else:
      newGrid.add((x, y))
    
  return newGrid

if __name__ == "__main__":
  with open("input.txt") as f:
    grid = set()
    instructionsIdx = 0
    lines = [x.strip() for x in f.readlines()]
    for (idx, line) in enumerate(lines):
      if line == "":
        instructionsIdx = idx + 1
        break
      [x, y] = line.split(',')
      grid.add((int(x), int(y)))

    firstInstruction = lines[instructionsIdx]
    newGrid = foldGrid(grid, firstInstruction)
    print(len(newGrid))

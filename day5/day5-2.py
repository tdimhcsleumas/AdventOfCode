from dataclasses import dataclass
import re
from collections import defaultdict


@dataclass
class Line():
  x1: int
  y1: int
  x2: int
  y2: int

def markPoints(matrix, line):
  dx = int(line.x2 != line.x1) * (-1 if line.x1 > line.x2 else 1)
  dy = int(line.y2 != line.y1) * (-1 if line.y1 > line.y2 else 1)

  x = line.x1
  y = line.y1
  while x != line.x2 or y != line.y2:
    matrix[(x,y)] += 1
    x += dx
    y += dy

  matrix[(x,y)] += 1

if __name__ == "__main__":

  filename = "input.txt"
  with open(filename) as f:
    filelines = f.readlines()
    matrix = defaultdict(lambda: 0)
    intersectionPoints = 0

    for fileline in filelines:
      m = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", fileline)
      x1 = int(m.group(1))
      y1 = int(m.group(2))
      x2 = int(m.group(3))
      y2 = int(m.group(4))

      markPoints(matrix, Line(x1, y1, x2, y2))


    for (idx, val) in matrix.items():
      intersectionPoints += val >= 2

    print(intersectionPoints)


    

def cost(pos, target):
  dx = 1 if target > pos else -1
  cost = 0
  steps = 1

  while pos != target:
    pos += dx
    cost += steps
    steps += 1

  return cost

if __name__ == "__main__":
  filename = "input.txt"
  with open(filename) as f:
    positions = [int(x) for x in f.readlines()[0].strip().split(",")]
    maxPosition = max(positions)
    crabPositions = [0] * (maxPosition + 1)
    for position in positions:
      crabPositions[position] += 1

    avgPosition = sum(positions) // len(positions)

    avgCost = sum(cost(pos, avgPosition) * count for pos, count in enumerate(crabPositions))

    upperCost = avgCost
    for position in range(avgPosition, maxPosition + 1):
      testCost = sum(cost(pos, position) * count for pos, count in enumerate(crabPositions)) 
      if avgCost < testCost: break
      upperCost = testCost

    lowerCost = avgCost
    for position in range(avgPosition, -1, -1):
      testCost = sum(cost(pos, position) * count for pos, count in enumerate(crabPositions)) 
      if avgCost < testCost: break
      lowerCost = testCost
      
    print(min(upperCost, lowerCost))

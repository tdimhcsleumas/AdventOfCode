if __name__ == "__main__":
  filename = "input.txt"
  with open(filename) as f:
    positions = [int(x) for x in f.readlines()[0].strip().split(",")]
    maxPosition = max(positions)
    crabPositions = [0] * (maxPosition + 1)
    for position in positions:
      crabPositions[position] += 1

    minCost = sum(pos * count for pos, count in enumerate(crabPositions))

    for position in range(1, maxPosition + 1):
      testCost = sum(abs(position - pos) * count for pos, count in enumerate(crabPositions)) 
      minCost = min(minCost, testCost)

    print(minCost)

if __name__ == "__main__":
  filename = "input.txt" 
  with open(filename) as f:
    lines = f.readlines()
    map = []

    for line in lines:
      map.append([int(x) for x in line.strip()])

    lowSum = 0
    for i in range(len(map)):
      for j in range(len(map[i])):
        if i > 0 and map[i-1][j] <= map[i][j]: continue
        if i < len(map) - 1 and map[i+1][j] <= map[i][j]: continue
        if j > 0 and map[i][j-1] <= map[i][j]: continue
        if j < len(map[i]) - 1 and map[i][j+1] <= map[i][j]: continue
        lowSum += map[i][j] + 1

    print(lowSum)
 

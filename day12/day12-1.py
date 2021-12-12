from collections import defaultdict

def findAllPaths(start, adjList, parentPath, visitedSet):
  if start in visitedSet:
    return []

  currentPath = parentPath + [start]
  if start == "end":
    return [currentPath]

  if start.islower():
    visitedSet.add(start)

  retList = []
  for vertex in adjList[start]:
    result = findAllPaths(vertex, adjList, currentPath, set(visitedSet))
    retList += result

  return retList

if __name__ == "__main__":
  filename = "input.txt"
  with open(filename) as f:
    adjList = defaultdict(lambda: list())
    for line in f.readlines():
      [x, y] = line.strip().split('-')
      adjList[x].append(y)
      adjList[y].append(x)

    resultList = findAllPaths("start", adjList, [], set())
    filtered = [x for x in resultList if len(x) != 0]
    print(len(filtered))



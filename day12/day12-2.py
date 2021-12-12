from collections import defaultdict

def findAllPaths(start, adjList, parentPath, visitedSet, twiceVertex):
  if start in visitedSet:
    return []

  currentPath = parentPath + [start]
  if start == "end":
    return [currentPath]


  retList = []

  if twiceVertex == None and start != "start":
    twiceSet = set(visitedSet)

    if twiceVertex == start:
      twiceSet.add(start)

    for vertex in adjList[start]:
      result = findAllPaths(vertex, adjList, currentPath, set(twiceSet), start)
      retList += result
  
  if start.islower():
    visitedSet.add(start)

  for vertex in adjList[start]:
    result = findAllPaths(vertex, adjList, currentPath, set(visitedSet), twiceVertex)
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

    resultList = findAllPaths("start", adjList, [], set(), None)
    filtered = [",".join(x) for x in resultList if len(x) != 0]

    # some duplicates
    print(len(set(filtered)))



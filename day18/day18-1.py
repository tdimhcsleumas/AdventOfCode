from math import ceil, floor
import json

def applyNeighbor(src: list, path: list, targetIdx: int, num: int):
  # move to the left neighbor, if it exists
  lastOne = None
  idx = len(path) - 1

  while idx >= 0:
    if path[idx] == targetIdx:
      lastOne = idx
      break
    idx -= 1

  if lastOne != None: # if there is a neighbor
    # walk down the array
    cur = src
    for x in range(lastOne):
      cur = cur[path[x]]

    idx = 0 if targetIdx == 1 else 1

    while type(cur[idx]) == list:
      cur = cur[idx]
      idx = targetIdx

    cur[idx] += num

def explode(src: list, a: list, path: list):
  [l, r] = a

  cur = src
  for x in path[:-1]:
    cur = cur[x]
  cur[path[-1]] = 0

  applyNeighbor(src, path, 1, l)
  applyNeighbor(src, path, 0, r)

def check_replace(a: list, path: list):
  [l, r] = a
  
  if type(l) == int and l >= 10:
    return (0, path)

  if type(l) == list:
    modified = check_replace(l, path.copy() + [0])
    if modified: return modified

  if type(r) == int and r >= 10:
    return (1, path)

  if type(r) == list:
    modified = check_replace(r, path.copy() + [1])
    if modified: return modified


def check_explode(a: list, path: list):
  [l, r] = a

  if len(path) == 4:
    return (a, path)

  if type(l) == list:
    modified = check_explode(l, path.copy() + [0])
    if modified: return modified

  if type(r) == list:
    modified = check_explode(r, path.copy() + [1])
    if modified: return modified

  return None

def check(src: list):
  while True:
    replace_result = check_replace(src, [])
    explode_result = check_explode(src, [])

    if explode_result:
      (a, path) = explode_result
      explode(src, a, path)

    elif replace_result:
      (a, path) = replace_result
      cur = src
      for x in path:
        cur = cur[x]
      value = cur[a]
      cur[a] = [floor(value / 2) , ceil(value / 2)]

    else:
      break

def sum(a, b):
  result = [a,b]
  check(result, result, [])

def magnitude(a):
  [l, r] = a

  lval = 0
  rval = 0

  if type(l) == int:
    lval = l
  else:
    lval = magnitude(l)

  if type(r) == int:
    rval = r
  else:
    rval = magnitude(r)

  return 3 * lval + 2 * rval

if __name__ == "__main__":
  with open("input.txt") as f:
    jsonString = '{"input":['
    jsonString += ','.join(line.strip() for line in f.readlines())
    jsonString += ']}'
    
    data = json.loads(jsonString)
    checkList = data["input"]
    sumValue = checkList[0]
    for value in checkList[1:]:
      sumValue = [sumValue, value]
      check(sumValue)

    print(sumValue)
    print(magnitude(sumValue))

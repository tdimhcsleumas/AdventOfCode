from re import search
from collections import defaultdict

if __name__ == "__main__":
  with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    template = lines[0]

    instructionMap = {}
    for instr in lines[2:]:
      m = search("(\w{2}) -> (\w)", instr)
      pair = m.group(1)
      inserted = m.group(2)
      instructionMap[pair] = inserted

    state = defaultdict(lambda: 0)
    freqMap = defaultdict(lambda: 0)

    for c in template:
      freqMap[c] += 1

    for i in range(len(template) - 1):
      pair = template[i] + template[i+1]
      state[pair] += 1

    for _ in range(40):
      newState = state.copy()
      for (pair, insertion) in instructionMap.items():
        if state[pair] > 0:
          times = state[pair]
          newState[pair] -= times
          newState[pair[0] + insertion] += times
          newState[insertion + pair[1]] += times
          freqMap[insertion] += times
      state = newState

    allItems = [x for x in freqMap.items()]
    maxItem = max(allItems, key=lambda x: x[1])
    minItem = min(allItems, key=lambda x: x[1])
    print(maxItem[1] - minItem[1])

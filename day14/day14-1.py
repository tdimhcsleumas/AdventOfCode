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

    print(template)
    for _ in range(10):

      newTemplate = ""
      for i in range(len(template) - 1):
        j = i + 1
        newTemplate += template[i]
        insertLetter = instructionMap.get(template[i] + template[j])
        if insertLetter:
          newTemplate += insertLetter
      
      newTemplate += template[-1]

      template = newTemplate

    freqMap = defaultdict(lambda: int())
    for c in template:
      freqMap[c] += 1

    allItems = [x for x in freqMap.items()]
    maxItem = max(allItems, key=lambda x: x[1])
    minItem = min(allItems, key=lambda x: x[1])
    print(maxItem[1] - minItem[1])



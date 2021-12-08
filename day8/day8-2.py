# generate brute list for brute force
def calcCandidateLists(sets):
  if len(sets) == 0: return [[]]
  currentSet = sets[0]
  candidateLists = []

  first, second = currentSet

  optionLists = calcCandidateLists(sets[1:]).copy()
  for optionList in optionLists:
    temp1 = optionList.copy()
    temp1.insert(0, first)
    temp1.insert(0, second)
    candidateLists.append(temp1)

    temp2 = optionList.copy()
    temp2.insert(0, second)
    temp2.insert(0, first)
    candidateLists.append(temp2)
  
  return candidateLists

lookupMap = {
  0b1110111: 0,
  0b0110000: 1,
  0b1101011: 2,
  0b1111001: 3,
  0b0111100: 4,
  0b1011101: 5,
  0b1011111: 6,
  0b1110000: 7,
  0b1111111: 8,
  0b1111101: 9
}

def lookupValue(input, encoding):
  checkValue = 0

  inputSet = set(input) 
  for value in encoding:
    checkValue <<= 1
    checkValue += value in inputSet

  return lookupMap.get(checkValue)

def isValid(inputList, encoding):
  validSet = set(lookupMap.keys())

  for input in inputList:
    checkValue = 0
    inputSet = set(input)
    for value in encoding:
      checkValue <<= 1
      checkValue += value in inputSet

    if not checkValue in validSet:
      return False
  
  return True

def parseInput(input):

  sortedInput = sorted(input, key=lambda x: len(x))

  # determine the inputs for 1 -> 7 -> 4 -> 8
  # use this to deduce the remaining ones
  top = None
  ur = set()
  mid = set()
  bot = set()

  # determine 1
  oneSignal = sortedInput[0] 
  sevenSignal = sortedInput[1]
  fourSignal = sortedInput[2]
  eightSignal = sortedInput[-1]

  # add left candidates
  for signal in oneSignal:
    ur.add(signal)

  # add top candidate
  for signal in sevenSignal:
    if signal in ur: continue
    top = signal

  # add mid and upper left candidates
  for signal in fourSignal:
    if signal in ur: continue
    mid.add(signal)

  # add lower left and bottom candidates
  for signal in eightSignal:
    if signal == top: continue
    if signal in mid: continue
    if signal in ur: continue
    bot.add(signal)

  currentSets = calcCandidateLists([list(ur), list(mid), list(bot)])
  checkSets = [[top] + x for x in currentSets]

  for checkSet in checkSets:
    if isValid(sortedInput, checkSet):
      return checkSet

if __name__ == "__main__":
  filename = "input.txt" 
  with open(filename) as f:

    outputSum = 0

    for line in f.readlines():
      [inputSection, outputSection] = line.strip().split("|")
      input = inputSection.strip().split(" ")
      outputs = outputSection.strip().split(" ")

      encoding = parseInput(input)
      tempSum = 0
      for output in outputs:
        tempSum *= 10
        tempSum += lookupValue(output, encoding)

      outputSum += tempSum

    print(outputSum)

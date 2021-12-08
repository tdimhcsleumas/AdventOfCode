
def findLineExtrema(lines, pos):
  bitLength = len(lines[0])
  zerosFreq = [0] * bitLength
  onesFreq = [0] * bitLength

  for line in lines:
    for i, c in enumerate(line):
      if c == "0":
        zerosFreq[i] += 1
      else:
        onesFreq[i] += 1

  if zerosFreq[pos] > onesFreq[pos]:
    return ("0", "1")
  else:
    return ("1", "0")

if __name__ == "__main__":
  filename = "./input.txt"


  with open(filename) as f:
    oxLines = [line.strip() for line in f.readlines()]
    carLines = oxLines.copy()
    bitCount = len(oxLines[0])

    for x in range(bitCount):
      if len(carLines) == 1 and len(oxLines) == 1:
        break

      if len(carLines) != 1:
        _, minBit = findLineExtrema(carLines, x)
        carLines = [line for line in carLines if line[x] == minBit]

      if len(oxLines) != 1:
        maxBit, _ = findLineExtrema(oxLines, x)
        oxLines = [line for line in oxLines if line[x] == maxBit]

    print(int(oxLines[0], 2) * int(carLines[0], 2))

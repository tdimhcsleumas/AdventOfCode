
if __name__ == "__main__":
  filename = "./input.txt"

  with open(filename) as f:
    lines = [line.strip() for line in f.readlines()]
    bitLength = len(lines[0])
    zerosFreq = [0] * bitLength
    onesFreq = [0] * bitLength

    for line in lines:
      for i, c in enumerate(line):
        if c == "0":
          zerosFreq[i] += 1
        else:
          onesFreq[i] += 1
    
    gammaStr = ""
    epsilonStr = ""

    for zeroFreq, oneFreq in zip(zerosFreq, onesFreq):
      if zeroFreq > oneFreq:
        gammaStr += "0"
        epsilonStr += "1"
      else:
        gammaStr += "1"
        epsilonStr += "0"

    print(int(gammaStr, 2) * int(epsilonStr, 2))
          
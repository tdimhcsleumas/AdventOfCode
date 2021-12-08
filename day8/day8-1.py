if __name__ == "__main__":
  filename = "input.txt" 
  with open(filename) as f:
    inputs = []
    outputs = []

    for line in f.readlines():
      [inputSection, outputSection] = line.strip().split("|")
      inputs.append(inputSection.strip().split(" "))
      outputs.append(outputSection.strip().split(" "))

    uniqueSet = set([2, 4, 3, 7])
    uniqueCount = 0

    for output in outputs:
      for segment in output:
        if segment in uniqueSet:
          print(segment)
        uniqueCount += len(segment) in uniqueSet

    print(uniqueCount)


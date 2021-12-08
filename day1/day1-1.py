#!/usr/bin/python3

if __name__ == "__main__":
  filename = "./input.txt"
  timesIncreased = 0
  windowSize = 3

  with open(filename) as f:
    lines = f.readlines()
    prevWindow = sum(int(x) for x in lines[0:windowSize])

    for i in range(windowSize, len(lines)):
      nextWindow = prevWindow - int(lines[i - windowSize]) + int(lines[i])
      timesIncreased = (prevWindow < nextWindow) + timesIncreased
      prevWindow = nextWindow

  print(timesIncreased)

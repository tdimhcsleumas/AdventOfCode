#!/usr/bin/python3

if __name__ == "__main__":
  filename = "./input.txt"
  timesIncreased = 0

  with open(filename) as f:
    lines = f.readlines()
    i = 1
    while i < len(lines):
      prev = int(lines[i-1])
      cur = int(lines[i])
      if (prev < cur):
        timesIncreased = timesIncreased + 1
      i = i + 1

  print(timesIncreased)

#!/usr/bin/python
import re

if __name__ == "__main__":
  filename = "./input.txt"
  horizontal = 0
  vertical = 0

  with open(filename) as f:
    for line in f.readlines():
      matches = re.search('(\w+) (\d+)', line)
      operation = matches.group(1)
      distance = int(matches.group(2))

      if operation == "forward":
        horizontal += distance
      else:
        multiplier = -1 if operation == "up" else 1
        vertical += distance * multiplier

  print(horizontal * vertical)

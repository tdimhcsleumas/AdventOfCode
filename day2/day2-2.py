#!/usr/bin/python
import re

if __name__ == "__main__":
  filename = "./input.txt"
  horizontal = 0
  vertical = 0
  aim = 0

  with open(filename) as f:
    for line in f.readlines():
      matches = re.search('(\w+) (\d+)', line)
      operation = matches.group(1)
      distance = int(matches.group(2))

      if operation == "forward":
        horizontal += distance
        vertical += aim * distance
      elif operation == "up":
        aim -= distance
      else:
        aim += distance

  print(horizontal * vertical)

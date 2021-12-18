from math import sqrt, floor, ceil

def inBounds(x, xBounds):
  return xBounds[0] <= x and xBounds[1] >= x

def validX(xBounds):
  n = ceil(-1/2 + sqrt(1/4 + 2 * min(xBounds)))

  # find all x values that will work
  validXs = []
  for x in range(n, xBounds[1] + 1):
    xVel = x
    xPos = 0
    prevXPos = 0
    t = 0
    validTs = []
    valid = False

    while True:
      if inBounds(xPos, xBounds):
        valid = True
        validTs.append(t)
        if xVel == 0: break

      t += 1
      xPos += xVel

      if xVel > 0:
        xVel -= 1
      elif xVel < 0:
        xVel += 1

      if prevXPos < xBounds[0] and xPos > xBounds[1] or \
         prevXPos > xBounds[1] and xPos < xBounds[0] or \
         valid and not inBounds(xPos, xBounds):
         break

    if valid:
      validXs.append((x, xVel, validTs))

  return validXs

def x(t):
  dx = 11
  pos = 0
  for _ in range(t):
    pos += dx
    if dx > 0: dx -= 1
    elif dx < 0: dx += 1
  return pos

if __name__ == "__main__":
  xBounds = [57, 116]
  yBounds = [-198, -148]

  validXs = validX(xBounds)
  print(validXs[0])

  y = 0
  maxYs = [] # represents the height and the t value that got to that height

  while True:
    yPos = 0
    dy = y

    localMax = 0
    validT = []
    valid = False
    t = 0

    while True:
      if inBounds(yPos, yBounds):
        valid = True
        validT.append(t)

      if yPos < min(yBounds) and dy < 0:
        break

      localMax = max(localMax, yPos)
      yPos += dy
      dy -= 1
      t += 1

    if valid and len(maxYs) and localMax < maxYs[-1][0]: # we've peaked
      break

    if valid:
      maxYs.append((localMax, validT, y))

    if len(maxYs) == 141:
      break

    y += 1

  print(maxYs)
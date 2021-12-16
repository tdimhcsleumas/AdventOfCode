from functools import reduce

def getVersion(packet):
  return int(packet[0:3], 2)

def getType(packet):
  return int(packet[3:6], 2) 

def handleLiteral(packet):
  number = 0
  idx = 6

  while True:
    isZero = packet[idx] == '0'
    idx += 1
    for _ in range(4):
      number <<= 1
      number |= int(packet[idx], 2)
      idx += 1

    if isZero: break

  return number, idx

versionSum = 0

def handleOperator(packet):
  global versionSum
  lengthTypeId = packet[6]
  instrCount = 0
  instrBits = 0
  thisType = getType(packet)
  values = []

  if lengthTypeId == '0':
    instrBits = int(packet[7:22], 2)
    idx = 22
  else:
    instrCount = int(packet[7:18], 2)
    idx = 18

  while True:
    version = getVersion(packet[idx:])
    type = getType(packet[idx:])

    versionSum += version

    if type == 4: # literal
      value, nextIdx = handleLiteral(packet[idx:])
    else:
      value, nextIdx = handleOperator(packet[idx:])

    instrBits -= nextIdx
    instrCount -= 1
    idx += nextIdx

    values.append(value)

    if instrCount == 0 and lengthTypeId == '1' or instrBits == 0 and lengthTypeId == '0':
      break

  if thisType == 0:
    value = sum(values)
  elif thisType == 1:
    value = reduce(lambda x,y: x * y, values, 1)
  elif thisType == 2:
    value = min(values)
  elif thisType == 3:
    value = max(values)
  elif thisType == 5:
    value = values[0] > values[1]
  elif thisType == 6:
    value = values[0] < values[1]
  else:
    value = values[0] == values[1]

  return int(value), idx


def parsePacket(packet):
  if packet == "": return
  global versionSum
  version = getVersion(packet)
  type = getType(packet)

  versionSum += version
  if type == 4: # literal
    value, _ = handleLiteral(packet)
  else:
    value, _ = handleOperator(packet)

  return value

if __name__ == "__main__":
  with open("input.txt") as f:
    testStr = f.readlines()[0].strip()
    binStr = ""

    for elem in testStr:
      binStr += format(int(elem, 16), '04b')

    value = parsePacket(binStr)

    print(f"version Sum: {value}")
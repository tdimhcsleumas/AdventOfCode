from dataclasses import dataclass
from collections import defaultdict
import json

@dataclass
class SolutionSet:
  values: list
  boardId: int
  selectedCount: int = 0

  def isWinner(self) -> bool:
    return self.selectedCount == 5

def parseBoards(lines: list) -> dict:
  ''' generate key -> SolutionSet[] mapping '''
  numberSolutionSetMap = defaultdict(lambda: [])
  boards = []

  while len(lines) > 0:
    board = []
    for i in range(5):
      row = [i for i in lines.pop(0).split(" ") if i != ""]
      board.append(row)
    boards.append(board)

  for idx, board in enumerate(boards):
    diagonalSet = SolutionSet([], idx, 0)

    for i in range(5):
      diagValue = board[i][i]
      diagonalSet.values.append(diagValue)
      numberSolutionSetMap[diagValue].append(diagonalSet)

      columnSet = SolutionSet([], idx, 0)
      rowSet = SolutionSet([], idx, 0)
      for j in range(5):
        rowVal = board[i][j]
        colVal = board[j][i]

        columnSet.values.append(colVal)
        rowSet.values.append(rowVal)

        numberSolutionSetMap[rowVal].append(rowSet)
        numberSolutionSetMap[colVal].append(columnSet)

  return numberSolutionSetMap, boards


def flattenBoard(board: list):
  flattened = []
  for i in range(5):
    for j in range(5):
      flattened.append(board[i][j])
  return flattened

  
if __name__ == "__main__":
  filename = "./input.txt"

  with open(filename) as f:
    lines = [line.strip() for line in f.readlines() if line != "\n"]
    bingoNumbers = lines[0].split(',')

    numberSolutionSetMap, boards = parseBoards(lines[1:])

    winningNumber = None
    boardsWonSet = set()
    seenSet = set()

    for bingoNumber in bingoNumbers:
      seenSet.add(bingoNumber)
      for solutionSet in numberSolutionSetMap[bingoNumber]:
        if not solutionSet.boardId in boardsWonSet:
          continue

        solutionSet.selectedCount += 1
        if solutionSet.selectedCount == 5:
          winningNumber = bingoNumber
          winningBoard = solutionSet.boardId
          solutionSet.alreadyWon = True
          boardsWonSet.add(winningBoard)

      if len(boardsWonSet) == len(boards):
        break

    print(int(winningNumber) * sum([int(v) for v in flattenBoard(boards[winningBoard]) if not v in seenSet]))



    



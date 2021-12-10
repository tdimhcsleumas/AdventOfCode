if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        score = 0
        scoreTable = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }
        startingSet = set(['(', '[', '{', '<'])
        endingStartingMap = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'
        }

        for line in lines:
            stack = []
            for c in line:
                if c in startingSet:
                    stack.append(c)
                elif endingStartingMap[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    print((stack[-1], c))
                    score += scoreTable[c]
                    break

        print(score)




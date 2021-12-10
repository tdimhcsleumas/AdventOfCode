if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        scores = []
        scoreTable = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4
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
            invalid = False
            score = 0
            for c in line:
                if c in startingSet:
                    stack.append(c)
                elif endingStartingMap[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    invalid = True
                    break

            if not invalid:
                for c in reversed(stack):
                    score *= 5
                    score += scoreTable[c]
                scores.append(score)

        print(sorted(scores)[(len(scores) - 1) // 2])




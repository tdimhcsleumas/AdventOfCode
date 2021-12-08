if __name__ == "__main__":
  filename = "input.txt"
  with open(filename) as f:
    initialState = [int(x) for x in f.readlines()[0].strip().split(",")]
    state = [0] * 9

    for item in initialState:
      state[item] += 1

    for itr in range(256):
      newState = state.copy()
      for idx in range(len(state)):
        if idx == 0:
          newState[idx] -= state[idx]
          newState[6] += state[idx]
          newState[8] += state[idx]
        else:
          newState[idx] -= state[idx]
          newState[idx - 1] += state[idx]
      state = newState

    print(sum(state))

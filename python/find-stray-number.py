# Use XOR to extract duplicate
def stray(arr):
    currentChar = 0
    for x in arr:
        currentChar ^= x
    return currentChar
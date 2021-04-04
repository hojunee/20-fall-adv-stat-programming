# Solution for Ex 8-4

def find(word, letter, start_idx):
    index = start_idx
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
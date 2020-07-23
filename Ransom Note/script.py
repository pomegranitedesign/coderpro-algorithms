# Created by Dmitriy Shin on July 22, 2020
from collections import defaultdict


def main():
    magazine = ['A', 'B', 'C', 'D', 'E', 'F']
    word = 'BED'
    print(canSpell(magazine, word))  # True
    print(canSpell(magazine, 'cat'))  # False


def canSpell(mag: list, word: str) -> bool:
    letters = defaultdict(int)
    for c in mag:
        letters[c] += 1
    for c in word:
        if letters[c] <= 0:
            return False
    return True


if __name__ == '__main__':
    main()

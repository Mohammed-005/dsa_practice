from collections import defaultdict

def group_of_anagrams_2(strs: list[str]) -> list[list[str]]:

    anagrams = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for char in word:
            index = ord(char) - ord('a')
            count[index] += 1

        anagrams[tuple(count)].append(word)

    return list(anagrams.values())


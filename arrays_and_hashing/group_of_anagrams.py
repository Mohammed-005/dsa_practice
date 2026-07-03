from collections import defaultdict

def group_of_anagrams(strs: list[str]) -> list[list[str]]:

    anagrams = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))

        anagrams[sorted_word].append(word)

    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
print(group_of_anagrams(strs))



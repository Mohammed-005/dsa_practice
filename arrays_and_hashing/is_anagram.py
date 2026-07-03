def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    counter_s = {}

    for char in s:
        counter_s[char] = counter_s.get(char, 0) + 1

    for char in t:

        if char not in counter_s or counter_s[char] == 0:
            return False

        else:
            counter_s[char] -= 1

    return True

s = 'listen'
t = 'silent'
print(is_anagram(s, t))
# 1456: Maximum Number of Vowels in a Subsrting of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Attempts: 2


def maxVowels(s: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    curr_index = 1
    max_length = len(s)
    max_vowels = 0

    # Window initialization
    for i in range(k):
        if s[i] in vowels:
            max_vowels += 1

    current_vowels = max_vowels
    while curr_index + k <= max_length:
        if s[curr_index - 1] in vowels:
            current_vowels -= 1
        if s[curr_index + k - 1] in vowels:
            current_vowels += 1

        # Maximum possible found, early return
        if current_vowels > max_vowels:
            max_vowels = current_vowels
        if max_vowels == k:
            return max_vowels
        curr_index += 1

    return max_vowels


### TEST CASES
print(maxVowels("abciiidef", 3))
print(maxVowels("aeiou", 2))
print(maxVowels("leetcode", 3))
print(maxVowels("weallloveyou", 7))

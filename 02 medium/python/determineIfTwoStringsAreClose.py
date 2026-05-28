# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/
# Attempts: 3


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    word1_hash = {}
    for c in word1:
        if c in word1_hash:
            word1_hash[c] += 1
        else:
            word1_hash[c] = 1

    word2_hash = {}
    for c in word2:
        if c in word2_hash:
            word2_hash[c] += 1
        else:
            word2_hash[c] = 1

    word1_dupe_count = {}
    word2_dupe_count = {}
    for k in word1_hash:
        if word1_hash[k] in word1_dupe_count:
            word1_dupe_count[word1_hash[k]] += 1
        else:
            word1_dupe_count[word1_hash[k]] = 1

    for k in word2_hash:
        if word2_hash[k] in word2_dupe_count:
            word2_dupe_count[word2_hash[k]] += 1
        else:
            word2_dupe_count[word2_hash[k]] = 1

    # Clearing letters
    for k in word1_dupe_count:
        if word1_dupe_count[k] != word2_dupe_count[k]:
            return False

    return True


### TEST CASES
print(closeStrings("abc", "bca"))
print(closeStrings("a", "aa"))
print(closeStrings("cabbba", "abbccc"))

# 1768. Merge Strings Alternatively
# https://leetcode.com/problems/merge-strings-alternately/description/
# Attempts: 1

def mergeAlternately(word1: str, word2: str) -> str:
    lowest = min(len(word1), len(word2))
    result = ""
    for i in range(0, lowest):
        result += word1[i]
        result += word2[i]

    result += word1[lowest:]
    result += word2[lowest:]

    return result

# Recursive solution
def mergeAltRecursive(word1: str, word2: str) -> str:
    if len(word1) == 0:
        return word2
    elif len(word2) == 0:
        return word1
    else:
        return word1[0] + word2[0] + mergeAltRecursive(word1[1:], word2[1:])

### TEST CODE
print(mergeAlternately(word1="abc", word2="pqr"))
print(mergeAlternately(word1="ab", word2="pqrs"))
print(mergeAlternately(word1="abcd", word2="pq"))

print(mergeAltRecursive(word1="abc", word2="pqr"))
print(mergeAltRecursive(word1="ab", word2="pqrs"))
print(mergeAltRecursive(word1="abcd", word2="pq"))

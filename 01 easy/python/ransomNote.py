# 383 https://leetcode.com/problems/ransom-note/description/
# Attempts: 

def canConstruct(ransomNote: str, magazine: str) -> bool:
    word_dictionary = {}
    for letter in magazine:
        if letter in word_dictionary:
            word_dictionary[letter] += 1
        else:
            word_dictionary[letter] = 1

    for letter in ransomNote:
        if letter not in word_dictionary:
            return False
        elif word_dictionary[letter] == 0:
            return False
        else:
            word_dictionary[letter] -= 1

    return True

### TEST CASES ### 
print(canConstruct('a', 'b'))
print(canConstruct('aa', 'ab'))
print(canConstruct('aa', 'aab'))

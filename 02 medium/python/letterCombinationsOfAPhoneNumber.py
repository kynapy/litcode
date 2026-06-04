# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Attempts: 1


from typing import List


def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    dictionary = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    return letterCombinationsHelper(digits, dictionary)


def letterCombinationsHelper(digits: str, dictionary: dict) -> List[str]:
    result = []
    if len(digits) == 1:
        for letter in dictionary[digits[0]]:
            result.append(letter)
        return result
    else:
        results = letterCombinationsHelper(digits[1:], dictionary)
        for letter in dictionary[digits[0]]:
            for back in results:
                result.append(letter + back)

    return result


### TEST CASES
print(letterCombinations("23"))
print(letterCombinations("234"))

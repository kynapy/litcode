# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/
# Attempts: 1


def reverseWords(s: str) -> str:
    result = ""
    current_word = ""
    for i in s:
        if i == " ":
            if current_word != "":
                result = current_word + " " + result
                current_word = ""
        else:
            current_word += i

    if current_word != "":
        result = current_word + " " + result
    return result[:-1]


def inPlaceReverseWords(s: str) -> str:

    return s


### TEST CASES
print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))

### TEST CASES (for in place challenge)
print(inPlaceReverseWords("the sky is blue"))
print(inPlaceReverseWords("  hello world  "))
print(inPlaceReverseWords("a good   example"))

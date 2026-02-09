# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# Attempts: 2


def reverseVowels(s: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    vowel_stack = []
    temp_string = ""
    result = ""

    for i in range(len(s)):
        if s[i].lower() in vowels:
            vowel_stack.append(s[i])
            temp_string += "_"
        else:
            temp_string += s[i]

    for i in range(len(temp_string)):
        if temp_string[i] == "_":
            result += vowel_stack.pop(-1)
        else:
            result += temp_string[i]
    return result


# Better solution implementation
def twoPointerReverseVowel(s: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    result_front = ""
    result_back = ""
    front = 0
    back = len(s) - 1
    while front <= back:
        curr_front = s[front]
        curr_back = s[back]
        if front == back:
            result_front += curr_front
            break
        if curr_front.lower() not in vowels:
            result_front += curr_front
            front += 1
        if curr_back.lower() not in vowels:
            result_back = curr_back + result_back
            back -= 1
        if curr_front.lower() in vowels and curr_back.lower() in vowels:
            result_front += curr_back
            result_back = curr_front + result_back
            front += 1
            back -= 1
    return result_front + result_back


### TEST CASES
print(reverseVowels("IceCreAm"))
print(reverseVowels("leetcode"))
print(reverseVowels(" "))


### TEST CASES
print(twoPointerReverseVowel("IceCreAm"))
print(twoPointerReverseVowel("leetcode"))
print(twoPointerReverseVowel(" "))
print(twoPointerReverseVowel("ai"))
print(twoPointerReverseVowel("lb"))
print(twoPointerReverseVowel("a."))
print(twoPointerReverseVowel(".a"))

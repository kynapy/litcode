# 415 https://leetcode.com/problems/add-strings/description/
# Attempts : 1

def convertToNumber(text: str) -> int:
    result = 0
    for i in range(1, len(text) + 1):
        result += int(text[-i]) * 10 ** (i - 1)
    return result

def convertToString(number: int) -> str:
    result = ''
    while number:
        remainder = number % 10
        number = number // 10
        result = str(remainder) + result
    return result if result else '0'

def addStrings(num1: str, num2: str) -> str:
    sum = convertToNumber(num1) + convertToNumber(num2)
    return convertToString(sum)


### TEST CASES
print(addStrings('11', '123'))
print(addStrings('456', '77'))
print(addStrings('0', '0'))


# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/
# Attempts: 3


def convert(s: str, numRows: int) -> str:
    result_list = []
    result = ""

    for _ in range(numRows):
        result_list.append([])

    count = 0
    increasing = True
    for letter in s:
        result_list[count].append(letter)

        if increasing and count + 1 < numRows:
            count += 1
        elif not increasing and count - 1 >= 0:
            count -= 1

        if count == 0:
            increasing = True
        if count == numRows - 1:
            increasing = False

    for row in result_list:
        for letter in row:
            result += letter

    return result


### TEST CASES
print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("A", 1))

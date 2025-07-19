# 278 https://leetcode.com/problems/first-bad-version/description/
# Attempts: 1

def firstBadVersion(n: int, bad: int) -> int:
    def isBadVersion(version: int, bad: int) -> bool:
        return version >= bad

    highest = n
    lowest = 1

    while highest != lowest:
        middle = (highest + lowest) // 2
        current_is_bad = isBadVersion(middle, bad)

        if current_is_bad:
            highest = middle
        else:
            lowest = middle + 1

    return lowest

### TEST CASES ###
print(firstBadVersion(5, 3))

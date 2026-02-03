# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
# Attempts: 3


def gcdOfString(str1: str, str2: str) -> str:
    shorter = ""
    if len(str1) > len(str2):
        shorter = str2
    else:
        shorter = str1

    for i in range(len(shorter)):
        current = ""
        if i == 0:
            current = shorter
        else:
            current = shorter[:-i]

        size = len(current)
        if isDivisor(str1, current) and isDivisor(str2, current):
            return current

    return ""


# Helper predicate function
def isDivisor(str1: str, divisor: str) -> bool:
    if len(str1) % len(divisor) == 0:
        comparator = divisor * (len(str1) // len(divisor))
        if comparator == str1:
            return True
    return False


### TEST
print(gcdOfString("ABCABC", "ABC"))
print(gcdOfString("ABABAB", "ABAB"))
print(gcdOfString("LEET", "CODE"))
print(gcdOfString("AAAAAB", "AAA"))
print(
    gcdOfString(
        "TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    )
)

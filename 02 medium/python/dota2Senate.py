# 649. Dota2 Senate
# https://leetcode.com/problems/dota2-senate/description/
# Attempts: 1


def predictPartyVictory(senate: str) -> str:
    sequence_queue = list(senate)
    ban_stack = []

    while sequence_queue:
        curr = sequence_queue.pop(0)
        if ban_stack:
            if ban_stack[-1] == curr:
                ban_stack.append(curr)
            else:
                sequence_queue.append(ban_stack.pop(-1))
        else:
            ban_stack.append(curr)

    if ban_stack[0] == "D":
        return "Dire"
    else:
        return "Radiant"


### TEST CASES
print(predictPartyVictory("RD"))
print(predictPartyVictory("RDD"))

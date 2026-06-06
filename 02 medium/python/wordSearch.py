# 79. Word Search
# https://leetcode.com/problems/word-search/description/
# Attempts: 1


from typing import List


def exist(board: List[List[str]], word: str) -> bool:

    def dfs(position, index, seen):
        if index >= len(word):
            return True

        seen.add(position)
        i = position[0]
        j = position[1]

        if i - 1 >= 0 and board[i - 1][j] == word[index] and (i - 1, j) not in seen:
            r = dfs((i - 1, j), index + 1, seen)
            if r:
                return True

        if (
            i + 1 < len(board)
            and board[i + 1][j] == word[index]
            and (i + 1, j) not in seen
        ):
            r = dfs((i + 1, j), index + 1, seen)
            if r:
                return True

        if j - 1 >= 0 and board[i][j - 1] == word[index] and (i, j - 1) not in seen:
            r = dfs((i, j - 1), index + 1, seen)
            if r:
                return True

        if (
            j + 1 < len(board[0])
            and board[i][j + 1] == word[index]
            and (i, j + 1) not in seen
        ):
            r = dfs((i, j + 1), index + 1, seen)
            if r:
                return True

        seen.remove(position)
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            position = (i, j)
            if board[i][j] == word[0]:
                seen = set()
                r = dfs(position, 1, seen)
                if r:
                    return True

    return False


### TEST CASES
print(
    exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
)

print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))

print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))

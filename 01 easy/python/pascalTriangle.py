class Solution:
    def generate(self, numRows):
        result = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        for i in range(numRows-2):
            rowResult = [1]
            prevRow = result[-1]
            for j in range(i+1):
                rowResult.append(prevRow[j] + prevRow[j+1])
            rowResult.append(1)
            result.append(rowResult)
        return result

print(Solution().generate(2))
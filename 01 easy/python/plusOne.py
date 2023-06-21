class Solution(object):
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            length = len(digits)
            sum = 1
            for i in digits:
                sum += i * pow(10, length-1)
                length -= 1
            sum = str(sum)
            result =[]
            for i in sum:
                result.append(int(i))
            return result

# Test cases
test = Solution()
print(test.plusOne([1,2,3]))
print(test.plusOne([4,3,2,1]))
print(test.plusOne([9]))
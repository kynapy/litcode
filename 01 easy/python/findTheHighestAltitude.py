class Solution(object):
    def largestAltitude(self, gain):
        currentAltitude = 0
        highestAltitude = 0
        for i in gain:
            currentAltitude += i
            if currentAltitude > highestAltitude:
                highestAltitude = currentAltitude

        return highestAltitude

# Test Cases
test = Solution()
print(test.largestAltitude([-5,1,5,0,-7]))
print(test.largestAltitude([-4,-3,-2,-1,4,3,2]))

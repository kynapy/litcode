class Solution(object):
    def checkStraightLine(self, coordinates):
        firstPoint = coordinates[0]
        secondPoint = coordinates[1]
        divisor = (secondPoint[0] - firstPoint[0])
        if divisor == 0:
            for i in range(len(coordinates) - 1):
                point = coordinates[i]
                nextPoint = coordinates[i + 1]
                difference = nextPoint[0] - point[0]
                if difference != 0:
                    return False
        else:
            gradient = (secondPoint[1] - firstPoint[1]) / divisor
            try:
                for i in range(len(coordinates) - 1):
                    point = coordinates[i]
                    nextPoint = coordinates[i + 1]
                    slope = (nextPoint[1] - point[1]) / (nextPoint[0] - point[0])
                    if slope != gradient:
                        return False
            except:
                return False
        return True
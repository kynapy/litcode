# 733 https://leetcode.com/problems/flood-fill/description/
# Attempts: 1

def checkValidSpot(image: list[list[int]], position: tuple) -> bool:
    if position[0] < 0 or position[1] < 0:
        return False
    if position[0] > len(image) - 1:
        return False
    if position[1] > len(image[0]) - 1:
        return False
    return True

def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    target = image[sr][sc]
    queue = []
    checked = set()
    queue.append((sr, sc))

    while queue:
        current_position = queue.pop(0)
        checked.add(current_position)
        current_value = image[current_position[0]][current_position[1]]
        
        if current_value == target:
            image[current_position[0]][current_position[1]] = color
            
            up = (current_position[0] - 1, current_position[1])
            down = (current_position[0] + 1, current_position[1])
            left = (current_position[0], current_position[1] - 1)
            right = (current_position[0], current_position[1] + 1)

            if checkValidSpot(image, up) and up not in checked:
                queue.append(up)
            if checkValidSpot(image, down) and down not in checked:
                queue.append((down))
            if checkValidSpot(image, left) and left not in checked:
                queue.append(left)
            if checkValidSpot(image, right) and right not in checked:
                queue.append(right)
 
    return image

### TEST CASES ###
print(floodFill([[1,1,1], [1,1,0], [1,0,1]], 1, 1, 2))
print(floodFill([[0,0,0], [0,0,0]], 0, 0, 0))

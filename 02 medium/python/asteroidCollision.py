# https://leetcode.com/problems/asteroid-collision/description/

def asteroidCollision(asteroids):
    stack = Stack()
    result = []
    for asteroid in asteroids:
        if asteroid >= 0:
            # Asteroid moving right
            stack.push(asteroid)
        else:
            # Asteroid moving left
            asteroid_destroyed = False
            while not asteroid_destroyed and stack.get_length() > 0:
                right_moving_asteroid = stack.pop()
                if right_moving_asteroid > (-asteroid):
                    asteroid_destroyed = True
                    stack.push(right_moving_asteroid)
                elif right_moving_asteroid == (-asteroid):
                    asteroid_destroyed = True
            if not asteroid_destroyed:
                result.append(asteroid)
    
    result.extend(stack.get_stack())
    return result

# Defined stack to use more relatable names of push and pop
# Also for practice
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def get_length(self):
        return len(self.stack)

    def get_stack(self):
        return self.stack

    def __str__(self) -> str:
        return ' '.join(str(x) for x in self.stack)

# Test cases
print(asteroidCollision([5, 10, -5]), end="\n")
print(asteroidCollision([8, -8]), end="\n")
print(asteroidCollision([10,2,-5]), end="\n")
print(asteroidCollision([-5, 10,2,-5]), end="\n")

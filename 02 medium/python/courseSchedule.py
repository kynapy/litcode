# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/
# Attempts:


from typing import List, Set


class Node:
    def __init__(self, val: int, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    node_hashmap = {}

    # Build Graph
    for prereq in prerequisites:
        course = prereq[0]
        req = prereq[1]

        course_node = None
        req_node = None

        if course not in node_hashmap:
            course_node = Node(course)
            node_hashmap[course] = course_node
        else:
            course_node = node_hashmap[course]

        if req not in node_hashmap:
            req_node = Node(req)
            node_hashmap[req] = req_node
        else:
            req_node = node_hashmap[req]

        course_node.neighbors.append(req_node)

    def dfs(node: Node, seen: Set, visited: Set):
        if node.val in visited:
            return False

        for neighbor in node.neighbors:
            if neighbor.val in seen:
                return True
            else:
                seen.add(neighbor.val)
                if dfs(neighbor, seen, visited):
                    return True

            seen.remove(neighbor.val)

        visited.add(node.val)
        return False

    visited = set()
    for val in node_hashmap:
        if val not in visited:
            seen = set()
            seen.add(val)
            cycle = dfs(node_hashmap[val], seen, visited)
            if cycle == True:
                return False

    return True


def optimizedCanFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    state = [0] * numCourses

    # Construct graph
    for course, req in prerequisites:
        graph[course].append(req)

    # Check for cycles
    # States:
    # - 0: Unvisited
    # - 1: Visited
    # - 2: Cleared of cycles

    def dfs(course: int) -> bool:
        if state[course] == 2:
            return False
        if state[course] == 1:
            return True

        state[course] = 1
        for req in graph[course]:
            if dfs(req) == True:
                return True

        state[course] = 2
        return False

    for course in range(len(graph)):
        if dfs(course):
            return False

    return True


### TEST CASES
print(canFinish(2, [[1, 0]]))
print(canFinish(2, [[1, 0], [0, 1]]))

# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/
# Attempts: 1

from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    obtained_keys = set([0])
    rooms_to_visit = []
    for key in rooms[0]:
        rooms_to_visit.append(key)
        obtained_keys.add(key)
    visited = 1

    while rooms_to_visit:
        key = rooms_to_visit.pop(0)
        visited += 1

        new_keys = rooms[key]
        for new_key in new_keys:
            if new_key not in obtained_keys:
                obtained_keys.add(new_key)
                rooms_to_visit.append(new_key)

        if visited == len(rooms):
            return True

    return False


### TEST CASES
print(canVisitAllRooms([[1], [2], [3], []]))
print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

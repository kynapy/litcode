# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# Attempts: 1

import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.array.append(val)
            self.hashmap[val] = len(self.array) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            last_item = self.array[-1]
            item_to_delete_index = self.hashmap[val]
            self.hashmap[last_item] = item_to_delete_index
            self.array[item_to_delete_index] = last_item
            del self.hashmap[val]
            self.array.pop(-1)
            return True
        else:
            return False

    def getRandom(self) -> int:
        length = len(self.array)
        random_index = random.randint(0, length - 1)
        return self.array[random_index]


# Insert is O(1): O(1) amoritized append to back of list, only when resizing is O(n), O(1) insert to hashmap
# Delete is O(1): O(1) delete from hashmap, delete from back of array is O(1)
# Random access is O(1) due to array

# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/
# Attempts: 1

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional["Node"]) -> Optional["Node"]:
    if not node:
        return None

    node_hashmap = {}
    queue = [node]

    while queue:
        curr = queue.pop(0)
        curr_new = None

        if curr.val not in node_hashmap:
            curr_new = Node(curr.val)
            node_hashmap[curr.val] = curr_new
        else:
            curr_new = node_hashmap[curr.val]

        for neighbor in curr.neighbors:
            new_neighbor = None
            if neighbor.val not in node_hashmap:
                new_neighbor = Node(neighbor.val)
                node_hashmap[neighbor.val] = new_neighbor
                queue.append(neighbor)
            else:
                new_neighbor = node_hashmap[neighbor.val]

            curr_new.neighbors.append(new_neighbor)

    return node_hashmap[node.val]

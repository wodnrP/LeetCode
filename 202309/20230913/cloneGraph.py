
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node):
        from collections import deque
        
        if node is None:
            return None
        
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for i in curr.neighbors:
                print(i.val)
                if i not in visited:
                    queue.appendleft(i)
                    visited[i] = Node(i.val)
                visited[curr].neighbors.append(visited[i])
        return visited[node]
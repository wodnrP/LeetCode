class Solution:
    def levelOrder(self, root):
        l=[]
        self.level_search(root, l)
        return l

    def level_search(self, node, l):
        queue = [(node, 0)]
        while queue:
            node, level = queue.pop(0)
            if node is not None:
                if len(l) < level+1:
                    l.append([])   
                l[level].append(node.val)
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
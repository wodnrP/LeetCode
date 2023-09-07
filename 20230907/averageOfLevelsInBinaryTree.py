class Solution:
    def averageOfLevels(self, root):
        l=[]
        self.level_search(root, l)
        print(l)
        l = [sum(i)/len(i) if len(i) >= 2 else sum(i) for i in l]
        return l

    def level_search(self, node, l):
        queue = [(node, 0)]
        while queue:
            node, level = queue.pop(0)
            if node is not None:
                if len(l) < level+1:
                    l.append([])
            
                l[level].append(node.val)

                if node.right:
                    queue.append((node.right, level+1))
                if node.left:
                    queue.append((node.left, level+1))

        return l
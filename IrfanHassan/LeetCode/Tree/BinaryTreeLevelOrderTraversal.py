def levelOrder(self, root):
        if not root: 
            return root
        queue, ans = [root], []
        while queue:
            ans += [ [node.val for node in queue] ]
            temp = []
            for node in queue:
                if node.left:
                    temp += [node.left]
                if node.right:
                    temp += [node.right]
            queue = temp
        return ans
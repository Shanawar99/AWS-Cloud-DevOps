def printTree(self, root: TreeNode) -> List[List[str]]:
        
        def getHeight(node=root):
            return 1+max(getHeight(node.left), getHeight(node.right)) if node else 0
        
        height = getHeight()-1
        columns = 2**(height+1)-1
        res = [[""]*columns for _ in range(height+1)]
        
        queue = deque([(root, (columns-1)//2)])
        r = 0
        
        while queue:
            for _ in range(len(queue)):
                node, c = queue.popleft()
                res[r][c] = str(node.val)
                if node.left:
                    queue.append((node.left, c-2**(height-r-1)))
                if node.right:
                    queue.append((node.right, c+2**(height-r-1)))
            r += 1
             
        return res
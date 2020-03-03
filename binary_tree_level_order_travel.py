class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                e = queue.pop(0)
                level.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            res.append(level)
        return res

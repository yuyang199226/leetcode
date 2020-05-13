#coding: utf-8
"""
验证是否是有效 二叉搜索树， 一种方法是 用中序遍历，拿到 列表，如果 该列表有序表示 是正确的，不能有相等的情况
另一种是递归 每个值都有一个区间 left 初始是 无穷小 right 是 无穷大


"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res= []
        self.helper(root, res)
        print(res)
        if len(res) == 0:
            return True
        prev = res[0]
        for i in range(1, len(res)):
            if res[i] <= prev:
                return False
            prev = res[i]
        return True


    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)




class Solution(object):
    def isValidBST(self, root, left=float('-inf'), right=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False

        return self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)



import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque([(root)])
        depth = 1
        while que:
            sz  = len(que)
            for i in range(0 ,sz):
                node = que.popleft()

                if node.left == None and node.right == None:
                    return depth
                if node.left! = None:
                    que.append((node.left))
                if node.right! = None:
                    que.append((node.right))
            depth+ =1
        return  depth







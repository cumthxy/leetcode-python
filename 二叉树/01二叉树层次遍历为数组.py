import queue
class Soulation():
    def printTree(self,root):
        result = [[]]
        q = queue.Queue()
        if root == None:
            return []
        q.put([root,0])
        while q.empty():
            temp = q.get()
            node = temp[0]
            level = temp[1]
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                q.put([node.left,level+1])
            if node.right:
                q.put([node.right,level+1])
        return result


